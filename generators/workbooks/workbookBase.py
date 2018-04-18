import xlsxwriter
from pathlib import Path


class WorkbookBase:
    workbook = ''

    def __init__(self, property_name):
        self.initialize_workbook(property_name)

    def initialize_workbook(self, property_name):
        sanitized_property_name = property_name.replace(':', '').replace('\\', '')
        outputFile = Path("./output").joinpath(sanitized_property_name).with_suffix(".xlsx")

        self.workbook = xlsxwriter.Workbook(outputFile)

    def close_workbook(self):
        self.workbook.close()
        return True
