from generators.worksheets.worksheet import Worksheet
from functools import reduce
import operator


class ContactsPopulator:
    @staticmethod
    def populate_project_contacts_sheet(worksheet: Worksheet, title_code, credits):

        contacts_cast = ContactsPopulator.populate_project_contacts_sheet_cast(worksheet, title_code, credits)
        contacts_crew = ContactsPopulator.populate_project_contacts_sheet_crew(worksheet, title_code, credits)

        contacts = reduce(operator.add, [contacts_cast, contacts_crew])
        return contacts

    @staticmethod
    def populate_project_contacts_sheet_cast(worksheet: Worksheet, title_code, credits):
        cast_order_cutoff = 5

        filtered_cast = list(filter(lambda d: d['order'] <= cast_order_cutoff, credits['cast']))

        contacts = []
        for person in filtered_cast:
            dataset = {
                'title_code': title_code,
                'name': person['name'],
                'role': 'Cast'
            }
            worksheet.write_data_row(dataset)
            contacts.append(person['name'])
        return contacts

    @staticmethod
    def populate_project_contacts_sheet_crew(worksheet: Worksheet, title_code, credits):
        whitelisted_crew_jobs = ['Director', 'Producer', 'Co-Producer', 'Writer', 'Executive Producer',
                                 'Consulting Producer', 'Screenplay']

        filtered_crew = list(filter(lambda d: d['job'] in whitelisted_crew_jobs, credits['crew']))

        contacts = []

        for person in filtered_crew:
            dataset = {
                'title_code': title_code,
                'name': person['name'],
                'role': person['job']
            }
            worksheet.write_data_row(dataset)
            contacts.append(person['name'])
        return contacts


        # rejected_crew = list(filter(lambda d: d['job'] not in whitelisted_crew_jobs, credits['crew']))
        #
        # for person in rejected_crew:
        #     print(person['job'])

    @staticmethod
    def populate_contacts_merged_sheet(workbook, credits):
        worksheet = workbook.get_contacts_merged_sheet().get_worksheet()

        for person in credits:
            dataset = {
                'name': person,
            }
            worksheet.write_data_row(dataset)
