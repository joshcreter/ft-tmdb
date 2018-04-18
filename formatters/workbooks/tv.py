from formatters.workbooks.workbook import Workbook
from formatters.worksheets.common.genres import GenreSheet
from formatters.worksheets.tv.title import TitleSheet
from formatters.worksheets.common.ratings import RatingsSheet
from formatters.worksheets.common.project_contacts import ProjectContactsSheet
from formatters.worksheets.common.countries_of_origin import CountriesOfOriginSheet


class WorkbookTV(Workbook):
    titleSheet = ''
    genreSheet = ''
    ratingsSheet = ''
    projectContactsSheet = ''
    countriesOfOriginSheet = ''

    def __init__(self, series_name):
        super().__init__(series_name)
        self.generate_workbook()

    def generate_workbook(self):
        self.titleSheet = TitleSheet(self.workbook)
        self.genreSheet = GenreSheet(self.workbook)
        self.ratingsSheet = RatingsSheet(self.workbook)
        self.projectContactsSheet = ProjectContactsSheet(self.workbook)
        self.countriesOfOriginSheet = CountriesOfOriginSheet(self.workbook)

    def get_title_sheet(self):
        return self.titleSheet

    def get_genre_sheet(self):
        return self.genreSheet

    def get_ratings_sheet(self):
        return self.ratingsSheet

    def get_project_contacts_sheet(self):
        return self.projectContactsSheet

    def get_countries_of_origin_sheet(self):
        return self.countriesOfOriginSheet