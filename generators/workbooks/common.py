from generators.workbooks.workbookBase import WorkbookBase
from generators.worksheets.common.genres import GenreSheet
from generators.worksheets.common.ratings import RatingsSheet
from generators.worksheets.common.project_contacts import ProjectContactsSheet
from generators.worksheets.common.countries_of_origin import CountriesOfOriginSheet
from generators.worksheets.common.application import ApplicationSheet


class WorkbookCommon(WorkbookBase):
    genreSheet = ''
    ratingsSheet = ''
    projectContactsSheet = ''
    countriesOfOriginSheet = ''
    applicationSheet = ''

    def __init__(self, property_name):
        super().__init__(property_name)
        self.generate_workbook()

    def generate_workbook(self):
        self.genreSheet = GenreSheet(self.workbook)
        self.ratingsSheet = RatingsSheet(self.workbook)
        self.projectContactsSheet = ProjectContactsSheet(self.workbook)
        self.countriesOfOriginSheet = CountriesOfOriginSheet(self.workbook)
        self.applicationSheet = ApplicationSheet(self.workbook)

    def get_genre_sheet(self):
        return self.genreSheet

    def get_ratings_sheet(self):
        return self.ratingsSheet

    def get_project_contacts_sheet(self):
        return self.projectContactsSheet

    def get_countries_of_origin_sheet(self):
        return self.countriesOfOriginSheet

    def get_application_sheet(self):
        return self.applicationSheet
