from generators.worksheets.worksheet import Worksheet


class TvSeriesSheet(Worksheet):
    name = 'Series'
    columns = {
        'title_code': {'label': 'TitleCode', 'width': 15.0},
        'raw_title': {'label': 'Raw Title', 'width': 30.0},
        'formatted_title': {'label': 'Title', 'width': 30.0},
        'type':  {'label': 'ProjectType', 'width': 10.0},
        'imdb_id': {'label': 'ImdbCode', 'width': 15.0},
        'production_status': {'label': 'Status', 'width': 30.0},
        'episode_run_time': {'label': 'RunningTime', 'width': 15.0},
        'episode_run_time_adjusted': {'label': 'AdjustedRunningTime', 'width': 15.0},
        'year_completed': {'label': 'YearCompleted', 'width': 15.0},
        'original_language': {'label': 'OriginalLanguage', 'width': 15.0},
        'budget': {'label': 'Budget', 'width': 15.0},
        'budget_currency': {'label': 'BudgetCurrency', 'width': 15.0},
        'homepage': {'label': 'OfficialWebSite', 'width': 30.0},
        'original_format': {'label': 'OriginalFormat', 'width': 15.0},
        'copyright_holder': {'label': 'CopyrightHolder', 'width': 30.0},
        'copyright_year': {'label': 'CopyrightYear', 'width': 15.0},
        'series_overview': {'label': 'Synopsis', 'width': 30.0},
        'series_title_aka1': {'label': 'AKA_1', 'width': 30.0},
        'series_title_aka2': {'label': 'AKA_2', 'width': 30.0},
        'season_count': {'label': 'NumberOfSeasons', 'width': 15.0},

    }

    def __init__(self, workbook):
        super().__init__(workbook)
