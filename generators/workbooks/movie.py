from generators.worksheets.movie.title import MovieTitleSheet
from generators.workbooks.common import WorkbookCommon


class WorkbookMovie(WorkbookCommon):
    movieTitleSheet = ''

    def __init__(self, property_name):
        super().__init__(property_name)
        self.generate_workbook_movie()

    def generate_workbook_movie(self):
        self.movieTitleSheet = MovieTitleSheet(self.workbook)

    def get_movie_title_sheet(self):
        return self.movieTitleSheet

