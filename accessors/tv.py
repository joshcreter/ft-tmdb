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

        col_genre = 1

        ###

        workbook = WorkbookTV(series_name)
        # workbook.generate_workbook(series_name)
        worksheet_title = workbook.get_title_sheet().get_worksheet()
        columns_title = workbook.get_title_sheet().get_columns()

        worksheet_genre = workbook.get_genre_sheet().get_worksheet()
        columns_genre = workbook.get_genre_sheet().get_columns()

        worksheet_ratings = workbook.get_rating_sheet().get_worksheet()
        columns_ratings = workbook.get_rating_sheet().get_columns()

        current_worksheet_title_row = 1
        current_worksheet_genre_row = 1
        current_worksheet_ratings_row = 1

        for season in series_info['seasons']:
            season_number = season['season_number']
            for episode_number in range(1, season['episode_count']+1):
                episode = tmdb.TV_Episodes(series_id=series_id, season_number=season_number, episode_number=episode_number)
                episode_info = episode.info()
                imdb_id = episode.external_ids()['imdb_id']
                print("{0:02d}x{1:02d}: {2}".format(season_number, episode_number, episode_info['name']))

                title_code = AccessImdbTVSeries.title_code_for_episode(series_id, season_number, episode_number)
                worksheet_title.write(current_worksheet_title_row, columns_title['title_code'], title_code)
                worksheet_title.write(current_worksheet_title_row, columns_title['title'], episode_info['name'])
                worksheet_title.write(current_worksheet_title_row, columns_title['type'], 'Episodes')
                worksheet_title.write(current_worksheet_title_row, columns_title['season_number'], season_number)
                worksheet_title.write(current_worksheet_title_row, columns_title['episode_number'], episode_number)
                worksheet_title.write(current_worksheet_title_row, columns_title['tmdb_id'], episode_info['id'])
                worksheet_title.write(current_worksheet_title_row, columns_title['imdb_id'], imdb_id)
                worksheet_title.write(current_worksheet_title_row, columns_title['air_date'], episode_info['air_date'])
                worksheet_title.write(current_worksheet_title_row, columns_title['production_code'], episode_info['production_code'])
                worksheet_title.write(current_worksheet_title_row, columns_title['synopsis'], episode_info['overview'])

                current_worksheet_title_row += 1

                for genre in genres:
                    worksheet_genre.write(current_worksheet_genre_row, 0, title_code)
                    worksheet_genre.write(current_worksheet_genre_row, col_genre, genre['name'])
                    current_worksheet_genre_row += 1

                worksheet_ratings.write(current_worksheet_ratings_row, columns_ratings['title_code'], title_code)
                worksheet_ratings.write(current_worksheet_ratings_row, columns_ratings['authority'], 'MPAA')
                worksheet_ratings.write(current_worksheet_ratings_row, columns_ratings['rating'], rating_US)

                current_worksheet_ratings_row += 1

        #         # cast = episode['cast']
        #
        #         # for person in cast:
        #         #     print(person)


        workbook.close_workbook()


