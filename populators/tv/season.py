from formatters.common import CommonFormatters


class TvSeasonPopulator:
    @staticmethod
    def populate_season_sheet(workbook, season, title_code, series_title_code, season_title_formatted):
        worksheet = workbook.get_tv_season_sheet().get_worksheet()

        dataset = {
            'title_code': title_code,
            'series_title_code': series_title_code,
            'title': season['name'],
            'formatted_title': season_title_formatted,
            'type': 'Season'
        }
        worksheet.write_data_row(dataset)



