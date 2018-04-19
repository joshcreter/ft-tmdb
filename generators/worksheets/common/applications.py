from generators.worksheets.worksheet import Worksheet


class ApplicationsSheet(Worksheet):
    name = 'Applications'
    columns = {
        'title_code': {'label': 'TitleCode', 'width': 15.0},
        'application': {'label': 'ApplicationName', 'width': 50.0}
    }

    def __init__(self, workbook):
        super().__init__(workbook)
