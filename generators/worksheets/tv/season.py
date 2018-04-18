from generators.worksheets.worksheet import Worksheet


class TvSeasonSheet(Worksheet):
    name = 'Season'
    columns = {
        # Start from the first cell. Rows and columns are zero indexed.
        'title_code': {'position': 0, 'label': 'Title Code', 'width': 15.0},
        'series_title_code': {'position': 1, 'label': 'Series Title Code', 'width': 15.0},
        'title': {'position': 2, 'label': 'Title', 'width': 30.0},
        'formatted_title': {'position': 3, 'label': 'Formatted Title', 'width': 30.0},
        'type':  {'position': 4, 'label': 'Type', 'width': 10.0}
    }

    def __init__(self, workbook):
        super().__init__(workbook)