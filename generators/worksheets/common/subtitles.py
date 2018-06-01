from generators.worksheets.worksheet import Worksheet


class SubtitlesSheet(Worksheet):
    name = 'Subtitles'
    columns = {
        'title_code': {'label': 'TitleCode', 'width': 15.0},
        'language': {'label': 'Language', 'width': 30.0}
    }

    def __init__(self, workbook):
        super().__init__(workbook)
