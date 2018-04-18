from formatters.common import CommonFormatters


class TvEpisodePopulator:
    @staticmethod
    def populate_episode_sheet(workbook, title_code, season_title_code, season_number, episode_number, episode, series_title_formatted):
        worksheet = workbook.get_tv_episode_sheet().get_worksheet()

        episode_info = episode.info()
        imdb_id = episode.external_ids()['imdb_id']
        formatted_title = "{0} - Season {1:02d} - Ep. {2:02d}".format(series_title_formatted,
                                                                      season_number,
                                                                      episode_number)

        dataset = {
            'title_code': title_code,
            'season_title_code': season_title_code,
            'title': episode_info['name'],
            'formatted_title': formatted_title,
            'type': 'Episodes',
            'season_number': season_number,
            'episode_number': episode_number,
            'tmdb_id': episode_info['id'],
            'imdb_id': imdb_id,
            'air_date': CommonFormatters.format_date(episode_info['air_date']),
            'production_code': episode_info['production_code'],
            'synopsis': episode_info['overview']
        }
        worksheet.write_data_row(dataset)

