class RatingsSheet:
    worksheet = ''
    workbook = ''
    header_format = ''
    columns = {
        # Start from the first cell. Rows and columns are zero indexed.
        'title_code': 0,
        'authority': 1,
        'rating': 2,
    }

    def __init__(self, workbook):
        self.workbook = workbook
        self.generate_worksheet()

    def generate_worksheet(self):
        header_format = self.workbook.add_format({'bg_color': 'green'})

        header_row = 0

        header_title_code = 'Title Code'
        header_authority = 'Authority'
        header_rating = 'Rating'

        self.header_format = self.workbook.add_format({'bg_color': 'green'})

        worksheet = self.workbook.add_worksheet('Ratings')

        worksheet.write(header_row, self.columns['title_code'], header_title_code, header_format)
        worksheet.write(header_row, self.columns['authority'], header_authority, header_format)
        worksheet.write(header_row, self.columns['rating'], header_rating, header_format)

        worksheet.set_column(self.columns['title_code'], self.columns['title_code'], 15.0)
        worksheet.set_column(self.columns['authority'], self.columns['authority'], 25.0)
        worksheet.set_column(self.columns['rating'], self.columns['rating'], 25.0)

        self.worksheet = worksheet

    def get_worksheet(self):
        return self.worksheet

    def get_columns(self):
        return self.columns
