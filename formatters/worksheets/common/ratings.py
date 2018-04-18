from formatters.worksheets.worksheet import Worksheet


class RatingsSheet(Worksheet):
    name = 'Ratings'
    columns = {
        # Start from the first cell. Rows and columns are zero indexed.
        'title_code': {'position': 0, 'label': 'Title Code', 'width': 15.0},
        'authority': {'position': 1, 'label': 'Authority', 'width': 25.0},
        'rating':  {'position': 2, 'label': 'Rating', 'width': 25.0}
    }

    def __init__(self, workbook):
        super().__init__(workbook)

