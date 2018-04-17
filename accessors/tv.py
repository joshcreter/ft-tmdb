import tmdbsimple as tmdb
tmdb.API_KEY = '9115e244e6f77d274bb345abc96fa420'

import pprint
# import xlsxwriter
from workbook.tv.tv import WorkbookTV

import logging

class AccessImdbTVSeries:

    @staticmethod
    def title_code_for_episode(series_id, season_number, episode_number):
        return "{0}-{1:02d}x{2:02d}".format(series_id, season_number, episode_number)


    @staticmethod
    def get_series(series_name):

        search = tmdb.Search()
        response = search.tv(query=series_name)
        # series = response[0]

        series_id = search.results[0]['id']
        series_info = tmdb.TV(series_id).info()

        genres = series_info['genres']
        content_ratings = tmdb.TV(series_id).content_ratings()

        rating_US = list(filter(lambda d: d['iso_3166_1'] == 'US', content_ratings['results']))[0]['rating']

        ###

        workbook = WorkbookTV(series_name)

        worksheet_title = workbook.get_title_sheet().get_worksheet()
        worksheet_genre = workbook.get_genre_sheet().get_worksheet()
        worksheet_ratings = workbook.get_rating_sheet().get_worksheet()

        for season in series_info['seasons']:
            season_number = season['season_number']
            for episode_number in range(1, season['episode_count']+1):
                episode = tmdb.TV_Episodes(series_id=series_id, season_number=season_number, episode_number=episode_number)
                episode_info = episode.info()
                imdb_id = episode.external_ids()['imdb_id']
                title_code = AccessImdbTVSeries.title_code_for_episode(series_id, season_number, episode_number)

                print("{0:02d}x{1:02d}: {2}".format(season_number, episode_number, episode_info['name']))

                title_dataset = {
                    'title_code': title_code,
                    'title': episode_info['name'],
                    'type': 'Episodes',
                    'season_number': season_number,
                    'episode_number': episode_number,
                    'tmdb_id':  episode_info['id'],
                    'imdb_id': imdb_id,
                    'air_date': episode_info['air_date'],
                    'production_code': episode_info['production_code'],
                    'synopsis': episode_info['overview']
                }

                worksheet_title.write_data_row(title_dataset)

                ratings_dataset = {
                    'title_code': title_code,
                    'authority': 'MPAA',
                    'rating': rating_US
                }

                worksheet_ratings.write_data_row(ratings_dataset)

                for genre in genres:
                    genre_dataset = {
                        'title_code': title_code,
                        'genre': genre['name']
                    }
                    worksheet_genre.write_data_row(genre_dataset)



        #         # cast = episode['cast']
        #
        #         # for person in cast:
        #         #     print(person)


        workbook.close_workbook()


