from generators.workbooks.tv import WorkbookTV
from populators.tv.series import TvSeriesPopulator
from populators.tv.season import TvSeasonPopulator
from populators.tv.episode import TvEpisodePopulator
from accessors.common import CommonAccessor
from formatters.common import CommonFormatters
from formatters.tv import TvFormatters
from mappers.mappers import Mappers
from populators.common import CommonPopulator
from populators.contacts import ContactsPopulator

class SeriesAccessor(CommonAccessor):
    def __init__(self):
        super().__init__()

    def search_and_process_series(self, raw_series_name):
        series_id = self.search_for_series(raw_series_name)

        if series_id:
            series = self.tmdb.TV(series_id)
            series_info = series.info()
            workbook = WorkbookTV(series_info['name'])

            self.process_series(series_id, workbook)

    def search_for_series(self, raw_series_name):

        search = self.tmdb.Search()
        response = search.tv(query=raw_series_name)
        series_id = search.results[0]['id']

        return series_id

    def process_series(self, series_id, workbook):
        series = self.tmdb.TV(series_id)
        series_info = series.info()
        series_imdb_id = series.external_ids()['imdb_id']

        formatted_series_name = CommonFormatters.format_project_title(series_info['name'])

        genres = Mappers.map_genres(series_info['genres'])
        origin_countries = Mappers.map_countries(self.tmdb.TV(series_id).info()['origin_country'])

        content_ratings = self.tmdb.TV(series_id).content_ratings()
        rating_US = list(filter(lambda d: d['iso_3166_1'] == 'US', content_ratings['results']))[0]['rating'].\
            replace('TV-PG', 'PG')

        series_title_code = series_imdb_id

        TvSeriesPopulator.populate_series_sheet(workbook, series, series_title_code, formatted_series_name,
                                                series_imdb_id)
        for season in series_info['seasons']:
            self.process_season(formatted_series_name, series_title_code, genres, origin_countries, rating_US, season,
                                series_id, series_imdb_id, workbook)

        workbook.close_workbook()

    def process_season(self, formatted_series_name, series_title_code, genres, origin_countries, rating_US, season,
                       series_id, series_imdb_id, workbook):

        season_number = season['season_number']
        season_title_code = "{0}-{1}".format(series_imdb_id, season_number)

        formatted_season_name = "{0} - Season {1:02d}".format(formatted_series_name, season_number)

        TvSeasonPopulator.populate_season_sheet(workbook, season, season_title_code, series_title_code,
                                                formatted_season_name)

        if season_number > 0 and season_number < 2:
            for episode_number in range(1, season['episode_count'] + 1):
                self.process_episode(episode_number, formatted_series_name, season_title_code, genres, origin_countries,
                                     rating_US, season_number, series_id, series_imdb_id, workbook)

    def process_episode(self, episode_number, formatted_series_name, season_title_code, genres, origin_countries,
                        rating_US, season_number, series_id, series_imdb_id, workbook):
        episode = self.tmdb.TV_Episodes(series_id=series_id, season_number=season_number,
                                        episode_number=episode_number)

        print("{0:02d}x{1:02d}: {2}".format(season_number, episode_number, episode.info()['name']))

        title_code = TvFormatters.format_tv_episode_title_code(series_imdb_id, season_number, episode_number)

        TvEpisodePopulator.populate_episode_sheet(workbook, title_code, season_title_code, season_number,
                                                  episode_number, episode, formatted_series_name)
        ContactsPopulator.populate_project_contacts_sheet(workbook, title_code, episode.credits())
        CommonPopulator.populate_ratings_sheet(workbook, title_code, rating_US)
        CommonPopulator.populate_genre_sheet(workbook, title_code, genres)
        CommonPopulator.populate_countries_of_origin_sheet(workbook, title_code, origin_countries)
        CommonPopulator.populate_application_sheet(workbook, title_code)
