from formatters.worksheets.worksheet import Worksheet


class ProjectContactsSheet(Worksheet):
    name = 'Project Contacts'
    columns = {
        # Start from the first cell. Rows and columns are zero indexed.
        'title_code': {'position': 0, 'label': 'Title Code', 'width': 15.0},
        'name': {'position': 1, 'label': 'Contact Name', 'width': 40.0},
        'role':  {'position': 2, 'label': 'Role', 'width': 25.0}
    }

    def __init__(self, workbook):
        super().__init__(workbook)

