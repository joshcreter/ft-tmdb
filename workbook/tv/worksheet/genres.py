class GenreSheet:
    worksheet = ''
    workbook = ''
    header_format = ''
    columns = {
        # Start from the first cell. Rows and columns are zero indexed.
        'title_code': 0,
        'genre': 1,
    }

    def __init__(self, workbook):
        self.workbook = workbook
        self.generate_worksheet()

    def generate_worksheet(self):
        header_format = self.workbook.add_format({'bg_color': 'green'})

        header_row = 0

        header_title_code = 'Title Code'
        header_genre = 'Genre'

        self.header_format = self.workbook.add_format({'bg_color': 'green'})

        worksheet = self.workbook.add_worksheet('Genre')

        worksheet.write(header_row, self.columns['title_code'], header_title_code, header_format)
        worksheet.write(header_row, self.columns['genre'], header_genre, header_format)

        worksheet.set_column(self.columns['title_code'], self.columns['title_code'], 15.0)
        worksheet.set_column(self.columns['genre'], self.columns['genre'], 25.0)

        self.worksheet = worksheet

    def get_worksheet(self):
        return self.worksheet

    def get_columns(self):
        return self.columns
