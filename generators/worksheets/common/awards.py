from generators.worksheets.worksheet import Worksheet


class AwardsSheet(Worksheet):
    name = 'Awards'
    columns = {
        'title_code': {'label': 'TitleCode', 'width': 15.0},
        'year': {'label': 'Year', 'width': 25.0},
        'result': {'label': 'AwardQualifier', 'width': 25.0},
        'organization': {'label': 'AwardDesignator', 'width': 50.0},
        'trophy': {'label': 'AwardName', 'width': 30.0},
        'category': {'label': 'AwardCategory', 'width': 100.0},
    }

    def __init__(self, workbook):
        super().__init__(workbook)