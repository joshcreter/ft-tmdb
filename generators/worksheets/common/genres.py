from generators.worksheets.worksheet import Worksheet


class GenresSheet(Worksheet):
    name = 'Genres'
    columns = {
        'title_code': {'label': 'TitleCode', 'width': 15.0},
        'genre': {'label': 'Genre', 'width': 25.0}
    }

    def __init__(self, workbook):
        super().__init__(workbook)
