from formatters.worksheets.worksheet import Worksheet


class CountriesOfOriginSheet(Worksheet):
    name = 'Countries of Origin'
    columns = {
        # Start from the first cell. Rows and columns are zero indexed.
        'title_code': {'position': 0, 'label': 'Title Code', 'width': 15.0},
        'country': {'position': 1, 'label': 'Country of Origin', 'width': 25.0}
    }

    def __init__(self, workbook):
        super().__init__(workbook)