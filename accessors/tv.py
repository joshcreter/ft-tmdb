import tmdbsimple as tmdb
from formatters.workbooks.tv import WorkbookTV
from populators.tv import TVPopulator
from populators.common import CommonPopulator

tmdb.API_KEY = '9115e244e6f77d274bb345abc96fa420'


class AccessImdbTVSeries:

    @staticmethod
    def title_code_for_episode(series_id, season_number, episode_number):
        return "{0}-{1:02d}x{2:02d}".format(series_id, season_number, episode_number)


    @staticmethod
    def search_and_process_series(raw_series_name):
        series_id = AccessImdbTVSeries.search_for_series(raw_series_name)

        if series_id:
            AccessImdbTVSeries.process_series(series_id)

    @staticmethod
    def search_for_series(raw_series_name):

        search = tmdb.Search()
        response = search.tv(query=raw_series_name)
        series_id = search.results[0]['id']

        return series_id

    @staticmethod
    def process_series(series_id):
        series_info = tmdb.TV(series_id).info()

        genres = series_info['genres']
        # origin_countries =


        content_ratings = tmdb.TV(series_id).content_ratings()
        rating_US = list(filter(lambda d: d['iso_3166_1'] == 'US', content_ratings['results']))[0]['rating']

        workbook = WorkbookTV(series_info['name'])

        for season in series_info['seasons']:
            season_number = season['season_number']
            for episode_number in range(1, season['episode_count']+1):
                episode = tmdb.TV_Episodes(series_id=series_id, season_number=season_number,
                                           episode_number=episode_number)
                title_code = AccessImdbTVSeries.title_code_for_episode(series_id, season_number, episode_number)

                print("{0:02d}x{1:02d}: {2}".format(season_number, episode_number, episode.info()['name']))

                TVPopulator.populate_title_sheet(workbook, title_code, season_number, episode_number,
                                                        episode)

                CommonPopulator.populate_project_contacts_sheet(workbook, title_code, episode.credits())

                CommonPopulator.populate_ratings_sheet(workbook, title_code, rating_US)

                CommonPopulator.populate_genre_sheet(workbook, title_code, genres)

        workbook.close_workbook()
