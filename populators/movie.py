class MoviePopulator:
    @staticmethod
    def populate_movie_title_sheet(workbook, title_code, season_number, episode_number, episode, series_title_formatted):
        worksheet_title = workbook.get_movie_title_sheet().get_worksheet()

        episode_info = episode.info()
        imdb_id = episode.external_ids()['imdb_id']
        formatted_title = "{0} - Season {1:02d} - Ep. {2:02d}".format(series_title_formatted,
                                                                      season_number,
                                                                      episode_number)

        title_dataset = {
            'title_code': title_code,
            'title': episode_info['name'],
            'formatted_title': formatted_title,
            'type': 'Episodes',
            'season_number': season_number,
            'episode_number': episode_number,
            'tmdb_id': episode_info['id'],
            'imdb_id': imdb_id,
            'air_date': episode_info['air_date'],
            'production_code': episode_info['production_code'],
            'synopsis': episode_info['overview']
        }
        worksheet_title.write_data_row(title_dataset)


