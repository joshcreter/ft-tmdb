from formatters import CommonFormatters, TvFormatters
from generators import WorkbookTV
import textwrap


class TvEpisodePopulator:
    @staticmethod
    def populate_episode_sheet(workbook: WorkbookTV, title_code, season_title_code, season_number, episode_number, episode,
                               series_title_formatted):
        worksheet = workbook.get_tv_episode_sheet().get_worksheet()

        episode_info = episode.info()
        imdb_id = episode.external_ids()['imdb_id']

        formatted_title = TvFormatters.format_tv_episode_title(series_title_formatted=series_title_formatted,
                                                               episode_number=episode_number,
                                                               season_number=season_number)
        dataset = {
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


