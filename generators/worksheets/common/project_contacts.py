from generators.worksheets.worksheet import Worksheet


class ProjectContactsSheet(Worksheet):
    name = 'Project Contacts'
    columns = {
        'title_code': {'label': 'TitleCode', 'width': 15.0},
        'name': {'label': 'Contact Name', 'width': 40.0},
        'role':  {'label': 'Role', 'width': 25.0}
    }

    def __init__(self, workbook):
        super().__init__(workbook)

