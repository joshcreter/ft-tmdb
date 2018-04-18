from generators.workbooks.common import WorkbookCommon
from generators.worksheets.tv.series import TvSeriesSheet
from generators.worksheets.tv.season import TvSeasonSheet
from generators.worksheets.tv.episode import TvEpisodeSheet


class WorkbookTV(WorkbookCommon):
    tvSeriesSheet = ''
    tvSeasonSheet = ''
    tvEpisodeSheet = ''

    def __init__(self, property_name):
        super().__init__(property_name)
        self.generate_workbook_tv()

    def generate_workbook_tv(self):
        self.tvSeriesSheet = TvSeriesSheet(self.workbook)
        self.tvSeasonSheet = TvSeasonSheet(self.workbook)
        self.tvEpisodeSheet = TvEpisodeSheet(self.workbook)

    def get_tv_series_sheet(self):
        return self.tvSeriesSheet

    def get_tv_season_sheet(self):
        return self.tvSeasonSheet

    def get_tv_episode_sheet(self):
        return self.tvEpisodeSheet

