class TitleSheet:
    worksheet = ''
    workbook = ''
    header_format = ''
    columns = {
        # Start from the first cell. Rows and columns are zero indexed.
        'title_code': 0,
        'title': 1,
        'type': 2,
        'season_number': 3,
        'episode_number': 4,
        'tmdb_id': 5,
        'imdb_id': 6,
        'air_date': 7,
        'production_code': 8,
        'synopsis': 9
    }

    def __init__(self, workbook):
        self.workbook = workbook
        self.generate_worksheet()

    def generate_worksheet(self):

        header_row = 0
        self.header_format = self.workbook.add_format({'bg_color': 'green'})

        header_title_code = 'Title Code'
        header_title = 'Title'
        header_type = 'Type'
        header_season_number = 'Season No'
        header_episode_number = 'Episode Number'
        header_tmdb_id = 'TMDB ID'
        header_imdb_id = 'IMDB ID'
        header_air_date = 'Air Date'
        header_production_code = 'Production Code'
        header_synopsis = 'Synopsis'

        worksheet = self.workbook.add_worksheet('Title')

        worksheet.write(header_row, self.columns['title_code'], header_title_code, self.header_format)
        worksheet.write(header_row, self.columns['title'], header_title, self.header_format)
        worksheet.write(header_row, self.columns['type'], header_type, self.header_format)
        worksheet.write(header_row, self.columns['season_number'], header_season_number, self.header_format)
        worksheet.write(header_row, self.columns['episode_number'], header_episode_number, self.header_format)
        worksheet.write(header_row, self.columns['tmdb_id'], header_tmdb_id, self.header_format)
        worksheet.write(header_row, self.columns['imdb_id'], header_imdb_id, self.header_format)
        worksheet.write(header_row, self.columns['air_date'], header_air_date, self.header_format)
        worksheet.write(header_row, self.columns['production_code'], header_production_code, self.header_format)
        worksheet.write(header_row, self.columns['synopsis'], header_synopsis, self.header_format)

        worksheet.set_column(self.columns['title_code'], self.columns['title_code'], 15.0)
        worksheet.set_column(self.columns['title'], self.columns['title'], 25.0)
        worksheet.set_column(self.columns['type'], self.columns['type'], 10.0)
        worksheet.set_column(self.columns['season_number'], self.columns['season_number'], 10.0)
        worksheet.set_column(self.columns['episode_number'], self.columns['episode_number'], 15.0)
        worksheet.set_column(self.columns['tmdb_id'], self.columns['tmdb_id'], 15.0)
        worksheet.set_column(self.columns['imdb_id'], self.columns['imdb_id'], 15.0)
        worksheet.set_column(self.columns['air_date'], self.columns['air_date'], 15.0)
        worksheet.set_column(self.columns['production_code'], self.columns['production_code'], 15.0)
        worksheet.set_column(self.columns['synopsis'], self.columns['synopsis'], 100.0)

        self.worksheet = worksheet

    def get_worksheet(self):
        return self.worksheet

    def get_columns(self):
        return self.columns
