from generators.worksheets.worksheet import Worksheet


class TvSeriesSheet(Worksheet):
    name = 'Series'
    columns = {
        # Start from the first cell. Rows and columns are zero indexed.
        'title_code': {'position': 0, 'label': 'Title Code', 'width': 15.0},
        'title': {'position': 1, 'label': 'Title', 'width': 30.0},
        'formatted_title': {'position': 2, 'label': 'Formatted Title', 'width': 30.0},
        'type':  {'position': 3, 'label': 'Type', 'width': 10.0},
        'imdb_id': {'position': 4, 'label': 'IMDB ID', 'width': 15.0},
    }

    def __init__(self, workbook):
        super().__init__(workbook)
