import xlsxwriter
from pathlib import Path
from workbook.tv.worksheet.genres import GenreSheet
from workbook.tv.worksheet.title import TitleSheet
from workbook.tv.worksheet.ratings import RatingsSheet


class WorkbookTV:
    workbook = ''
    titleSheet = ''
    genreSheet = ''
    ratingSheet = ''

    def __init__(self, series_name):
        self.generate_workbook(series_name)

    def generate_workbook(self, series_name):
        outputFile = Path("./output").joinpath(series_name).with_suffix(".xlsx")

        self.workbook = xlsxwriter.Workbook(outputFile)
        # worksheet_title = AccessImdbTVSeries.generate_worksheet_title(workbook)

        self.titleSheet = TitleSheet(self.workbook)
        self.genreSheet = GenreSheet(self.workbook)
        self.ratingSheet = RatingsSheet(self.workbook)

    def get_title_sheet(self):
        return self.titleSheet

    def get_genre_sheet(self):
        return self.genreSheet

    def get_rating_sheet(self):
        return self.ratingSheet

    def close_workbook(self):
        self.workbook.close()
        return True
