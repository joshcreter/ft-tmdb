from workbook.workbook import Workbook
from workbook.tv.worksheets.genres import GenreSheet
from workbook.tv.worksheets.title import TitleSheet
from workbook.tv.worksheets.ratings import RatingsSheet


class WorkbookTV(Workbook):
    titleSheet = ''
    genreSheet = ''
    ratingSheet = ''

    def __init__(self, series_name):
        super().__init__(series_name)
        self.generate_workbook()

    def generate_workbook(self):
        self.titleSheet = TitleSheet(self.workbook)
        self.genreSheet = GenreSheet(self.workbook)
        self.ratingSheet = RatingsSheet(self.workbook)

    def get_title_sheet(self):
        return self.titleSheet

    def get_genre_sheet(self):
        return self.genreSheet

    def get_rating_sheet(self):
        return self.ratingSheet
