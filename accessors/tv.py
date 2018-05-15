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

    def search_and_process_series(self, raw_series_name, unique_id_start=None):
        series_id = self.search_for_series(raw_series_name)
        
        unique_id = unique_id_start

        if series_id:
            series = self.tmdb.TV(series_id)
            series_info = series.info()
            
            workbook = WorkbookTV(series_info['name'])

            self.process_series(series_id, workbook, unique_id)

            workbook.close_workbook()

    def search_for_series(self, raw_series_name):

        search = self.tmdb.Search()
        response = search.tv(query=raw_series_name)
        series_id = search.results[0]['id']

        return series_id

    def process_series(self, series_id, workbook, unique_id=None):
        series = self.tmdb.TV(series_id)
        series_info = series.info()
        series_imdb_id = series.external_ids()['imdb_id']

        formatted_series_name = CommonFormatters.format_project_title(series_info['name'])

        genres = Mappers.map_genres(series_info['genres'])
        origin_countries = Mappers.map_countries(self.tmdb.TV(series_id).info()['origin_country'])

        content_ratings = self.tmdb.TV(series_id).content_ratings()
        # rating_US = list(filter(lambda d: d['iso_3166_1'] == 'US', content_ratings['results']))[0]['rating'].\
        #     replace('TV-PG', 'PG')

        rating_US = None
        series_title_code = series_imdb_id

        TvSeriesPopulator.populate_series_sheet(workbook, series, series_title_code, formatted_series_name,
                                                series_imdb_id, unique_id)

        # unique_id_series = unique_id
        # unique_id_series = "7acd9516-3343-e811-9450-0a8d4423fe52"
        # if unique_id:
        #     unique_id += 1

        unique_id = formatted_series_name
        unique_id_series = formatted_series_name

        # unique_id="d9b9d190-f695-492e-bd56-997b6cda27f3"
        for season in series_info['seasons']:
            # if season['season_number'] > 0 and season['season_number'] < 2:
            if season['season_number'] > 0:

                unique_id = self.process_season(formatted_series_name, series_title_code, genres, origin_countries, rating_US, season,
                                    series_id, series_imdb_id, workbook, unique_id, unique_id_series)
        
        return unique_id

    def process_season(self, formatted_series_name, series_title_code, genres, origin_countries, rating_US, season,
                       series_id, series_imdb_id, workbook, unique_id=None, unique_id_series=None):

        season_number = season['season_number']
        season_title_code = "{0}-{1}".format(series_imdb_id, season_number)

        formatted_season_name = "{0} - Season {1:02d}".format(formatted_series_name, season_number)

        TvSeasonPopulator.populate_season_sheet(workbook, season, season_title_code, series_title_code,
                                                formatted_season_name, unique_id, unique_id_series)
        
        # unique_id_season = unique_id
        unique_id_season = formatted_season_name
        # if unique_id:
        #     unique_id += 1

        # for episode_number in range(1, 2):
        for episode_number in range(1, season['episode_count'] + 1):
            unique_id = self.process_episode(episode_number, formatted_series_name, season_title_code, genres, origin_countries,
                                 rating_US, season_number, series_id, series_imdb_id, workbook, unique_id,
                                             unique_id_season)
            
        return unique_id

    def process_episode(self, episode_number, formatted_series_name, season_title_code, genres, origin_countries,
                        rating_US, season_number, series_id, series_imdb_id, workbook, unique_id=None, 
                        unique_id_season=None):
        episode = self.tmdb.TV_Episodes(series_id=series_id, season_number=season_number,
                                        episode_number=episode_number)

        print("{0:02d}x{1:02d}: {2}".format(season_number, episode_number, episode.info()['name']))

        title_code = TvFormatters.format_tv_episode_title_code(series_imdb_id, season_number, episode_number)

        TvEpisodePopulator.populate_episode_sheet(workbook, title_code, season_title_code, season_number,
                                                  episode_number, episode, formatted_series_name, unique_id,
                                                  unique_id_season)
        ContactsPopulator.populate_project_contacts_sheet(workbook, title_code, episode.credits())
        CommonPopulator.populate_ratings_sheet(workbook, title_code, rating_US)
        CommonPopulator.populate_genres_sheet(workbook, title_code, genres)
        CommonPopulator.populate_countries_of_origin_sheet(workbook, title_code, origin_countries)
        CommonPopulator.populate_applications_sheet(workbook, title_code)
        # 
        # if unique_id:
        #     unique_id += 1
        #     
        return unique_id
            
