from formatters.common import CommonFormatters


class TvSeasonPopulator:
    @staticmethod
    def populate_season_sheet(workbook, season, title_code, series_title_code, season_title_formatted, unique_id=None,
                              parent_id=None):
        worksheet = workbook.get_tv_season_sheet().get_worksheet()

        dataset = {
            'unique_id': unique_id,
            'parent_id': parent_id,
            'title_code': title_code,
            'series_title_code': series_title_code,
            'title': season['name'],
            'formatted_title': season_title_formatted,
            'type': 'Seasons'
        }
        worksheet.write_data_row(dataset)



