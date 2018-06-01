from generators.workbooks import WorkbookBase
from generators.worksheets import *


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
    languagesSheet = ''
    subtitlesSheet = ''

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
        self.localizationsSheet = LocalizationsSheet(self.workbook)
        self.timelineSheet = TimelineSheet(self.workbook)
        self.awardsSheet = AwardsSheet(self.workbook)
        self.contactsMergedSheet = ContactsMergedSheet(self.workbook)
        self.languagesSheet = LanguagesSheet(self.workbook)
        self.subtitlesSheet = SubtitlesSheet(self.workbook)

    def get_genre_sheet(self) -> GenresSheet:
        return self.genreSheet

    def get_ratings_sheet(self) -> RatingsSheet:
        return self.ratingsSheet

    def get_project_contacts_sheet(self) -> ProjectContactsSheet:
        return self.projectContactsSheet

    def get_countries_of_origin_sheet(self) -> CountriesOfOriginSheet:
        return self.countriesOfOriginSheet

    def get_application_sheet(self) -> ApplicationsSheet:
        return self.applicationSheet

    def get_project_groups_sheet(self) -> ProjectGroupsSheet:
        return self.projectGroupsSheet

    def get_localizations_sheet(self) -> LocalizationsSheet:
        return self.localizationsSheet

    def get_timeline_sheet(self) -> TimelineSheet:
        return self.timelineSheet

    def get_awards_sheet(self) -> AwardsSheet:
        return self.awardsSheet

    def get_contacts_merged_sheet(self) -> ContactsMergedSheet:
        return self.contactsMergedSheet

    def get_languages_sheet(self) -> LanguagesSheet:
        return self.languagesSheet

    def get_subtitles_sheet(self) -> SubtitlesSheet:
        return self.subtitlesSheet

