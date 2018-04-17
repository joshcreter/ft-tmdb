from workbook.worksheet import Worksheet


class GenreSheet(Worksheet):
    name = 'Genre'
    columns = {
        # Start from the first cell. Rows and columns are zero indexed.
        'title_code': {'position': 0, 'label': 'Title Code', 'width': 15.0},
        'genre': {'position': 1, 'label': 'Genre', 'width': 25.0}
    }

    def __init__(self, workbook):
        super().__init__(workbook)
