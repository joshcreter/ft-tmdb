import xlsxwriter
from pathlib import Path


class Workbook:
    workbook = ''

    def __init__(self, property_name):
        self.initialize_workbook(property_name)

    def initialize_workbook(self, property_name):
        outputFile = Path("./output").joinpath(property_name).with_suffix(".xlsx")

        self.workbook = xlsxwriter.Workbook(outputFile)

    def close_workbook(self):
        self.workbook.close()
        return True
