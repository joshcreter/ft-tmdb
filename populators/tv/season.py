from formatters.common import CommonFormatters
import tmdbsimple as tmdb
from generators.workbooks.tv import WorkbookTV


class TvSeasonPopulator:
    @staticmethod
    def populate_season_sheet(workbook: WorkbookTV, title_code: str, series_title_code: str,
                              season_title_formatted: str,
                              parent_id: str=None):
        worksheet = workbook.get_tv_season_sheet().get_worksheet()

        dataset = {
            'parent_id': parent_id,
            'title_code': title_code,
            'series_title_code': series_title_code,
            'formatted_title': season_title_formatted,
            'type': 'Seasons'
        }
        worksheet.write_data_row(dataset)



