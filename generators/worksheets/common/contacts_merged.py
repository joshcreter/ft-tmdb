from generators.worksheets.worksheet import Worksheet


class ContactsMergedSheet(Worksheet):
    name = 'Contacts Merged'
    columns = {
        'name': {'label': 'Name', 'width': 40.0},
    }

    def __init__(self, workbook):
        super().__init__(workbook)

