from generators.worksheets.worksheet import Worksheet


class TimelineSheet(Worksheet):
    name = 'Timeline'
    columns = {
        'title_code': {'label': 'TitleCode', 'width': 15.0},
        'type': {'label': 'Type', 'width': 25.0},
        'media': {'label': 'Media', 'width': 25.0},
        'territory': {'label': 'Territory', 'width': 50.0},
        'start_date': {'label': 'StartDate', 'width': 30.0},
        'note': {'label': 'Note', 'width': 30.0},
    }

    def __init__(self, workbook):
        super().__init__(workbook)
