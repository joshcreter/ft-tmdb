from generators import WorkbookTV


class TvSeriesPopulator:
    @staticmethod
    def populate_series_sheet(workbook: WorkbookTV,
                              raw_title: str,
                              title_code: str,
                              series_title_formatted: str,
                              imdb_id: str,
                              production_status: str,
                              episode_run_time: int,
                              episode_run_time_adjusted: int,
                              year_completed: str,
                              original_language: str,
                              homepage: str,
                              copyright_holder: str,
                              copyright_year: str,
                              budget: str,
                              budget_currency: str,
                              original_format: str,
                              series_overview=str,
                              series_title_aka1=str,
                              series_title_aka2=str
                              ):

        worksheet = workbook.get_tv_series_sheet().get_worksheet()

        dataset = {
            'title_code': title_code,
            'title': raw_title,
            'formatted_title': series_title_formatted,
            'type': 'Series',
            'imdb_id': imdb_id,
            'production_status': production_status,
            'episode_run_time': episode_run_time,
            'episode_run_time_adjusted': episode_run_time_adjusted,
            'year_completed': year_completed,
            'original_language': original_language,
            'homepage': homepage,
            'copyright_holder': copyright_holder,
            'copyright_year': copyright_year,
            'budget': budget,
            'budget_currency': budget_currency,
            'original_format': original_format,
            'series_overview': series_overview,
            'series_title_aka1': series_title_aka1,
            'series_title_aka2': series_title_aka2
        }
        worksheet.write_data_row(dataset)
