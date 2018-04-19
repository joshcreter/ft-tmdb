from formatters.common import CommonFormatters
import textwrap

class TvEpisodePopulator:
    @staticmethod
    def populate_episode_sheet(workbook, title_code, season_title_code, season_number, episode_number, episode,
                               series_title_formatted, unique_id=None, parent_id=None):
        worksheet = workbook.get_tv_episode_sheet().get_worksheet()

        episode_info = episode.info()
        imdb_id = episode.external_ids()['imdb_id']
        # formatted_title = "{0} - Season {1:02d} - Ep. {2:02d}".format(series_title_formatted,
        #                                                               season_number,
        #                                                               episode_number)

        formatted_title = "{0} - Season {1} - Ep. {2}".format(series_title_formatted,
                                                                      season_number,
                                                                      episode_number)

        # formatted_title = "{0} - Season {1:02d} - Ep.{2}".format(series_title_formatted, season_number, episode_number)

        dataset = {
            'unique_id': unique_id,
            'parent_id': parent_id,
            'title_code': title_code,
            'season_title_code': season_title_code,
            'logline': episode_info['name'],
            'title': formatted_title,
            'type': 'Episodes',
            'season_number': season_number,
            'episode_number': episode_number,
            'tmdb_id': episode_info['id'],
            'imdb_id': imdb_id,
            'air_date': CommonFormatters.format_date(episode_info['air_date']),
            'production_code': episode_info['production_code'],
            'synopsis': textwrap.shorten(episode_info['overview'], width=999, placeholder="...")
        }
        worksheet.write_data_row(dataset)


