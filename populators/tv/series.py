class TvSeriesPopulator:
    @staticmethod
    def populate_series_sheet(workbook, series, title_code, series_title_formatted, imdb_id, unique_id=None):
        worksheet = workbook.get_tv_series_sheet().get_worksheet()

        series_info = series.info()

        dataset = {
            'unique_id': unique_id,
            'title_code': title_code,
            'title': series_info['name'],
            'formatted_title': series_title_formatted,
            'type': 'Series',
            'imdb_id': imdb_id
        }
        worksheet.write_data_row(dataset)


