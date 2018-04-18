from accessors.common import CommonAccessor
from generators.workbooks.movie import WorkbookMovie
from populators.common import CommonPopulator
from populators.contacts import ContactsPopulator
from formatters.common import CommonFormatters
from formatters.movie import MovieFormatters
from mappers.mappers import Mappers


class MovieAccessor(CommonAccessor):
    def __init__(self):
        super().__init__()

    def search_and_process_movielist(self, movielist):
        workbook = WorkbookMovie("movies")

        with open(movielist, 'r') as f:
            for movie in f:
                movie = movie.strip()

                self.search_and_process_movie(movie, workbook)

        workbook.close_workbook()

    def search_and_process_movie(self, raw_movie_name, workbook=None):
        movie_id = self.search_for_movie(raw_movie_name)

        if movie_id:
            project = self.tmdb.Movies(movie_id)
            property_info = project.info()

            property_title = property_info['title']

            print(property_title)

            if workbook:
                self.process_movie(project, property_title, workbook)

            else:
                workbook = WorkbookMovie(property_title)
                self.process_movie(project, property_title, workbook)
                workbook.close_workbook()

    def search_for_movie(self, raw_movie_name):

        search = self.tmdb.Search()
        response = search.movie(query=raw_movie_name)
        movie_id = search.results[0]['id']

        return movie_id

    def process_movie(self, project, property_title, workbook):
        property_info = project.info()

        imdb_id = project.external_ids()['imdb_id']

        formatted_property_name = CommonFormatters.format_project_title(property_title)

        title_code = imdb_id

        genres = Mappers.map_genres(property_info['genres'])

        origin_countries = Mappers.map_countries(
            company['origin_country'] for company in property_info['production_companies'])


        # content_ratings = property.content_ratings()
        # rating_US = list(filter(lambda d: d['iso_3166_1'] == 'US', content_ratings['results']))[0]['rating'].\
        #     replace('TV-PG', 'PG')

        #             TVPopulator.populate_title_sheet(workbook, title_code, season_number, episode_number,
        #                                                     episode, formatted_series_name)
        #

        ContactsPopulator.populate_project_contacts_sheet(workbook, title_code, project.credits())

        # CommonPopulator.populate_ratings_sheet(workbook, title_code, rating_US)

        CommonPopulator.populate_genre_sheet(workbook, title_code, genres)

        CommonPopulator.populate_countries_of_origin_sheet(workbook, title_code, origin_countries)

        CommonPopulator.populate_application_sheet(workbook, title_code)
