from generators.worksheets.worksheet import Worksheet


class ApplicationSheet(Worksheet):
    name = 'Application'
    columns = {
        # Start from the first cell. Rows and columns are zero indexed.
        'title_code': {'position': 0, 'label': 'Title Code', 'width': 15.0},
        'application': {'position': 1, 'label': 'Application Name', 'width': 50.0}
    }

    def __init__(self, workbook):
        super().__init__(workbook)
