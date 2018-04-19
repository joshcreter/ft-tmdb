from generators.worksheets.worksheet import Worksheet


class ProjectGroupsSheet(Worksheet):
    name = 'Project Groups'
    columns = {
        'title_code': {'label': 'TitleCode', 'width': 15.0},
        'project_group': {'label': 'ProjectGroup', 'width': 50.0}
    }

    def __init__(self, workbook):
        super().__init__(workbook)
