from generators.worksheets.worksheet import Worksheet


class MovieTitleSheet(Worksheet):
    name = 'Title'
    columns = {
        # 'unique_id': {'label': 'UniqueId', 'width': 15.0},
        'title_code': {'label': 'TitleCode', 'width': 15.0},
        # 'title': {'label': 'TitleUnformatted', 'width': 30.0},
        'formatted_title': {'label': 'Title', 'width': 30.0},
        'tagline': {'label': 'Logline', 'width': 60.0},
        'type':  {'label': 'ProjectType', 'width': 10.0},
        'imdb_id': {'label': 'ImdbCode', 'width': 15.0},
        'year_completed': {'label': 'YearCompleted', 'width': 15.0},
        'budget': {'label': 'Budget', 'width': 15.0},
        'budget_currency': {'label': 'BudgetCurrency', 'width': 15.0},
        'revenue': {'label': 'BoxOfficeEarningsNote', 'width': 15.0},
        'revenue_currency': {'label': 'BoxOfficeCurrency', 'width': 15.0},
        'runtime': {'label': 'RunningTime', 'width': 10.0},
        'homepage': {'label': 'OfficialWebSite', 'width': 30.0},
        'original_language':  {'label': 'OriginalLanguage', 'width': 10.0},
        'synopsis': {'label': 'ShortSynopsis', 'width': 100.0},
        'original_format': {'label': 'OriginalFormat', 'width': 15.0},
    }

    def __init__(self, workbook):
        super().__init__(workbook)
