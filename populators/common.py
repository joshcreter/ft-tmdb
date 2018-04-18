class CommonPopulator:
    @staticmethod
    def populate_application_sheet(workbook, title_code):
        worksheet = workbook.get_application_sheet().get_worksheet()

        applications = ['Avails', 'BizAffairs', 'InvenTrack']
        for application in applications:
            dataset = {
                'title_code': title_code,
                'application': application
            }
            worksheet.write_data_row(dataset)


    @staticmethod
    def populate_ratings_sheet(workbook, title_code, rating_US):
        worksheet_ratings = workbook.get_ratings_sheet().get_worksheet()
        ratings_dataset = {
            'title_code': title_code,
            'authority': 'MPAA',
            'rating': rating_US
        }
        worksheet_ratings.write_data_row(ratings_dataset)

    @staticmethod
    def populate_genre_sheet(workbook, title_code, genres):
        worksheet_genre = workbook.get_genre_sheet().get_worksheet()
        for genre in genres:
            genre_dataset = {
                'title_code': title_code,
                'genre': genre
            }
            worksheet_genre.write_data_row(genre_dataset)

    @staticmethod
    def populate_countries_of_origin_sheet(workbook, title_code, countries):
        worksheet = workbook.get_countries_of_origin_sheet().get_worksheet()
        for country in countries:
            dataset = {
                'title_code': title_code,
                'country': country
            }
            worksheet.write_data_row(dataset)