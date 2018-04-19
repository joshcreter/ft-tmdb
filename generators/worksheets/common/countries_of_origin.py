from generators.worksheets.worksheet import Worksheet


class CountriesOfOriginSheet(Worksheet):
    name = 'Countries of Origin'
    columns = {
        'title_code': {'label': 'TitleCode', 'width': 15.0},
        'country': {'label': 'Country', 'width': 25.0}
    }

    def __init__(self, workbook):
        super().__init__(workbook)
