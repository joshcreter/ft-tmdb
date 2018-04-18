
class CommonPopulator:
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
                'genre': genre['name']
            }
            worksheet_genre.write_data_row(genre_dataset)

    @staticmethod
    def populate_project_contacts_sheet(workbook, title_code, credits):
        CommonPopulator.populate_project_contacts_sheet_cast(workbook, title_code, credits)
        CommonPopulator.populate_project_contacts_sheet_crew(workbook, title_code, credits)

    def populate_project_contacts_sheet_cast(workbook, title_code, credits):
        worksheet = workbook.get_project_contacts_sheet().get_worksheet()

        cast_order_cutoff = 5

        filtered_cast = list(filter(lambda d: d['order'] <= cast_order_cutoff, credits['cast']))

        for person in filtered_cast:
            dataset = {
                'title_code': title_code,
                'name': person['name'],
                'role': 'Cast'
            }
            worksheet.write_data_row(dataset)


    def populate_project_contacts_sheet_crew(workbook, title_code, credits):
        worksheet = workbook.get_project_contacts_sheet().get_worksheet()

        whitelisted_crew_jobs = ['Director', 'Producer', 'Co-Producer', 'Writer', 'Executive Producer',
                                 'Consulting Producer']

        filtered_crew = list(filter(lambda d: d['job'] in whitelisted_crew_jobs, credits['crew']))

        for person in filtered_crew:
            dataset = {
                'title_code': title_code,
                'name': person['name'],
                'role': person['job']
            }
            worksheet.write_data_row(dataset)

        # rejected_crew = list(filter(lambda d: d['job'] not in whitelisted_crew_jobs, credits['crew']))
        #
        # for person in rejected_crew:
        #     print(person['job'])
