from generators.worksheets.worksheet import Worksheet


class LocalizationSheet(Worksheet):
    name = 'Localizations'
    columns = {
        'title_code': {'label': 'TitleCode', 'width': 15.0},
        'culture': {'label': 'CultureCode', 'width': 25.0},
        'title': {'label': 'Title', 'width': 30.0},
        'synopsis': {'label': 'Synopsis', 'width': 100.0}
    }

    def __init__(self, workbook):
        super().__init__(workbook)
