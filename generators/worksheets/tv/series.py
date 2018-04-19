from generators.worksheets.worksheet import Worksheet


class TvSeriesSheet(Worksheet):
    name = 'Series'
    columns = {
        'unique_id': {'label': 'Unique ID', 'width': 15.0},
        'title_code': {'label': 'Title Code', 'width': 15.0},
        'title': {'label': 'Title', 'width': 30.0},
        'formatted_title': {'label': 'Formatted Title', 'width': 30.0},
        'type':  {'label': 'Type', 'width': 10.0},
        'imdb_id': {'label': 'IMDB ID', 'width': 15.0},
    }

    def __init__(self, workbook):
        super().__init__(workbook)
