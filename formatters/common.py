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
        output_date = datetime.strptime(input_date, "%Y-%m-%d").date().strftime("%m/%d/%Y")

        return output_date