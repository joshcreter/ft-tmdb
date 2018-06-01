from accessors.common import CommonAccessor
from generators import WorkbookMovie
from populators import CommonPopulator, ContactsPopulator, MovieTitlePopulator
from formatters import CommonFormatters, MovieFormatters
from mappers import CommonMappers, CountryMapper
from accessors.awards import AwardsAccessor
from functools import reduce
import operator
from more_itertools import unique_everseen


class MovieAccessor(CommonAccessor):
    def __init__(self):
        super().__init__()

    def search_and_process_movielist(self, movielist):
        workbook = WorkbookMovie("movies")

        merged_contacts = []

        with open(movielist, 'r') as f:
            for movie in f:
                movie = movie.strip()

                contacts = self.search_and_process_movie(movie, workbook)
                merged_contacts.append(contacts)

        merged_contacts = reduce(operator.add, merged_contacts)
        merged_contacts = list(unique_everseen(merged_contacts))

        ContactsPopulator.populate_contacts_merged_sheet(workbook, merged_contacts)

        workbook.close_workbook()

    def search_and_process_movie(self, raw_movie_name, workbook=None):
        movie_id = self.search_for_movie(raw_movie_name)

        if movie_id:
            project = self.tmdb.Movies(movie_id)
            property_info = project.info()

            property_title = property_info['title']

            print(property_title)

            contacts = []
            if workbook:
                contacts = self.process_movie(project, property_title, workbook)

            else:
                workbook = WorkbookMovie(property_title)
                contacts = self.process_movie(project, property_title, workbook)
                workbook.close_workbook()

            return contacts

    def search_for_movie(self, raw_movie_name):

        search = self.tmdb.Search()
        response = search.movie(query=raw_movie_name)
        movie_id = search.results[0]['id']

        return movie_id

    def process_movie(self, movie, property_title, workbook):
        movie_info = movie.info()

        imdb_id = movie.external_ids()['imdb_id']

        awards = AwardsAccessor.get_awards(imdb_id)

        formatted_property_name = CommonFormatters.format_project_title(property_title)

        title_code = imdb_id

        genres = CommonMappers.map_genres(movie_info['genres'])
        release_dates = CommonMappers.map_release_dates(movie.release_dates())

        # origin_countries = Mappers.map_countries(
        #     company['origin_country'] for company in movie_info['production_companies'])
        origin_countries = CountryMapper.map_countries(country['iso_3166_1'] for country in movie_info['production_countries'])

        localizations = movie.translations()

        # content_ratings = property.content_ratings()
        # rating_US = list(filter(lambda d: d['iso_3166_1'] == 'US', content_ratings['results']))[0]['rating'].\
        #     replace('TV-PG', 'PG')

        rating_US = list(filter(lambda d: d['iso_3166_1'] == 'US', movie.releases()['countries']))[0]['certification'].\
            replace('TV-PG', 'PG')

        MovieTitlePopulator.populate_movie_title_sheet(workbook, title_code, movie, imdb_id)

        contacts = ContactsPopulator.populate_project_contacts_sheet(workbook, title_code, movie.credits())
        CommonPopulator.populate_genres_sheet(workbook, title_code, genres)
        CommonPopulator.populate_countries_of_origin_sheet(workbook, title_code, origin_countries)
        CommonPopulator.populate_applications_sheet(workbook, title_code)
        CommonPopulator.populate_project_groups_sheet(workbook, title_code)
        CommonPopulator.populate_ratings_sheet_US_only(workbook, title_code, rating_US)
        CommonPopulator.populate_localizations_sheet(workbook, title_code, localizations, property_title)
        CommonPopulator.populate_timeline_sheet(workbook, title_code, release_dates)
        CommonPopulator.populate_awards_sheet(workbook, title_code, awards)

        return(contacts)