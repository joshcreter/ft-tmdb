class TVPopulator:
    @staticmethod
    def populate_title_sheet(workbook, title_code, season_number, episode_number, episode):
        worksheet_title = workbook.get_title_sheet().get_worksheet()

        episode_info = episode.info()
        imdb_id = episode.external_ids()['imdb_id']

        title_dataset = {
            'title_code': title_code,
            'title': episode_info['name'],
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


