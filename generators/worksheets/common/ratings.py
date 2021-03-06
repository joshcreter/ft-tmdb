from generators.worksheets.worksheet import Worksheet


class RatingsSheet(Worksheet):
    name = 'Ratings'
    columns = {
        'title_code': {'label': 'TitleCode', 'width': 15.0},
        'authority': {'label': 'RatingAuthority', 'width': 25.0},
        'rating':  {'label': 'Rating', 'width': 25.0}
    }

    def __init__(self, workbook):
        super().__init__(workbook)

