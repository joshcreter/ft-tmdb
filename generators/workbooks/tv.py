from generators.workbooks.common import WorkbookCommon
from generators.worksheets.tv.series import TvSeriesSheet
from generators.worksheets.tv.season import TvSeasonSheet
from generators.worksheets.tv.episode import TvEpisodeSheet
from generators.worksheets.tv.season_contacts import SeasonContactsSheet
from generators.worksheets.tv.episode_contacts import EpisodeContactsSheet
from generators.worksheets.tv.series_contacts import SeriesContactsSheet


class WorkbookTV(WorkbookCommon):
    tvSeriesSheet = ''
    tvSeasonSheet = ''
    tvEpisodeSheet = ''
    tvEpisodeContactsSheet = ''
    tvSeasonContactsSheet = ''
    tvSeriesContactsSheet = ''

    def __init__(self, property_name):
        super().__init__(property_name)
        self.generate_workbook_tv()

    def generate_workbook_tv(self):
        self.tvSeriesSheet = TvSeriesSheet(self.workbook)
        self.tvSeasonSheet = TvSeasonSheet(self.workbook)
        self.tvEpisodeSheet = TvEpisodeSheet(self.workbook)
        self.tvEpisodeContactsSheet = EpisodeContactsSheet(self.workbook)
        self.tvSeasonContactsSheet = SeasonContactsSheet(self.workbook)
        self.tvSeriesContactsSheet = SeriesContactsSheet(self.workbook)

    def get_tv_series_sheet(self):
        return self.tvSeriesSheet

    def get_tv_season_sheet(self):
        return self.tvSeasonSheet

    def get_tv_episode_sheet(self):
        return self.tvEpisodeSheet

    def get_tv_episode_contacts_sheet(self):
        return self.tvEpisodeContactsSheet

    def get_tv_season_contacts_sheet(self):
        return self.tvSeasonContactsSheet

    def get_tv_series_contacts_sheet(self):
        return self.tvSeriesContactsSheet
