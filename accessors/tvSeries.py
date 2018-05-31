from generators.workbooks.tv import WorkbookTV
from accessors.common import CommonAccessor
from populators import ContactsPopulator
# import tmdbsimple as tmdb
import accessors.tv.series


class TvSeriesAccessor(CommonAccessor):
    def __init__(self):
        super().__init__()

    def search_and_process_series(self, raw_series_name: str):
        series_id = self.search_for_series(raw_series_name)

        if series_id:
            series = self.tmdb.TV(series_id)
            series_info = series.info()
            
            workbook = WorkbookTV(series_info['name'])

            series_contacts = accessors.tv.series.process_series(self, series, workbook)

            ContactsPopulator.populate_contacts_merged_sheet(workbook, series_contacts)

            workbook.close_workbook()

    def search_for_series(self, raw_series_name: str):
        search = self.tmdb.Search()
        search.tv(query=raw_series_name)
        series_id = search.results[0]['id']

        return series_id


