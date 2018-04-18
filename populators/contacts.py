class ContactsPopulator:
    @staticmethod
    def populate_project_contacts_sheet(workbook, title_code, credits):
        ContactsPopulator.populate_project_contacts_sheet_cast(workbook, title_code, credits)
        ContactsPopulator.populate_project_contacts_sheet_crew(workbook, title_code, credits)

    @staticmethod
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

    @staticmethod
    def populate_project_contacts_sheet_crew(workbook, title_code, credits):
        worksheet = workbook.get_project_contacts_sheet().get_worksheet()

        whitelisted_crew_jobs = ['Director', 'Producer', 'Co-Producer', 'Writer', 'Executive Producer',
                                 'Consulting Producer', 'Screenplay']

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
