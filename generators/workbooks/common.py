from generators.workbooks.workbookBase import WorkbookBase
from generators.worksheets.common.genres import GenresSheet
from generators.worksheets.common.ratings import RatingsSheet
from generators.worksheets.common.project_contacts import ProjectContactsSheet
from generators.worksheets.common.countries_of_origin import CountriesOfOriginSheet
from generators.worksheets.common.applications import ApplicationsSheet
from generators.worksheets.common.project_groups import ProjectGroupsSheet
from generators.worksheets.common.localizations import LocalizationSheet
from generators.worksheets.common.timeline import TimelineSheet
from generators.worksheets.common.awards import AwardsSheet
from generators.worksheets.common.contacts_merged import ContactsMergedSheet


class WorkbookCommon(WorkbookBase):
    genreSheet = ''
    ratingsSheet = ''
    projectContactsSheet = ''
    countriesOfOriginSheet = ''
    applicationSheet = ''
    projectGroupsSheet = ''
    localizationsSheet = ''
    timelineSheet = ''
    awardsSheet = ''
    contactsMergedSheet = ''

    def __init__(self, property_name):
        super().__init__(property_name)
        self.generate_workbook()

    def generate_workbook(self):
        self.genreSheet = GenresSheet(self.workbook)
        self.ratingsSheet = RatingsSheet(self.workbook)
        self.projectContactsSheet = ProjectContactsSheet(self.workbook)
        self.countriesOfOriginSheet = CountriesOfOriginSheet(self.workbook)
        self.applicationSheet = ApplicationsSheet(self.workbook)
        self.projectGroupsSheet = ProjectGroupsSheet(self.workbook)
        self.localizationsSheet = LocalizationSheet(self.workbook)
        self.timelineSheet = TimelineSheet(self.workbook)
        self.awardsSheet = AwardsSheet(self.workbook)
        self.contactsMergedSheet = ContactsMergedSheet(self.workbook)

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

    def get_project_groups_sheet(self):
        return self.projectGroupsSheet

    def get_localizations_sheet(self):
        return self.localizationsSheet

    def get_timeline_sheet(self):
        return self.timelineSheet

    def get_awards_sheet(self):
        return self.awardsSheet

    def get_contacts_merged_sheet(self):
        return self.contactsMergedSheet
