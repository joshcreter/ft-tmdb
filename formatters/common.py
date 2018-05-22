import re
from datetime import date, datetime


class CommonFormatters:
    @staticmethod
    def format_project_title(project_title):
        project_title = re.sub(r'^The (.*)', r'\1, The', project_title)
        project_title = re.sub(r'^A (.*)', r'\1, A', project_title)
        project_title = re.sub(r'^An (.*)', r'\1, An', project_title)

        return project_title

    @staticmethod
    def format_date(input_date):
        if "T" in input_date:
            input_date = input_date[:input_date.index("T")]

        output_date = datetime.strptime(input_date, "%Y-%m-%d").date().strftime("%m/%d/%Y")

        return output_date

    @staticmethod
    def format_date_year_only(input_date):
        if "T" in input_date:
            input_date = input_date[:input_date.index("T")]

        output_date = datetime.strptime(input_date, "%Y-%m-%d").date().strftime("%Y")

        return output_date

    @staticmethod
    def format_language(input_language):
        mapping = {
            'en': 'English'
        }

        output = mapping.get(input_language, None)
        return output

    @staticmethod
    def format_project_status(status):
        mapping = {
            'Planned': 'Development',
            'In Production': 'Production',
            'Post Production': 'Post-Production',
            'Released': 'Catalog'
        }

        output = mapping.get(status, None)
        return output
