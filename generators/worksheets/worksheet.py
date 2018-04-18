class Worksheet:
    _worksheet = ''
    columns = {}
    workbook = ''
    header_row = 0
    current_row = 1

    def __init__(self, workbook):
        self.workbook = workbook
        self.generate_worksheet()

    def write_header_cell(self, worksheet, column_data):
        header_format = self.workbook.add_format({'bg_color': 'green'})

        worksheet.write(self.header_row, column_data['position'], column_data['label'], header_format)
        worksheet.set_column(column_data['position'],  column_data['position'],  column_data['width'])

    def generate_worksheet(self):
        worksheet = self.workbook.add_worksheet(self.name)

        for column_data in self.columns:
            self.write_header_cell(worksheet, self.columns[column_data])

        self._worksheet = worksheet

    def get_worksheet(self):
        return self

    def get_columns(self):
        return self.columns

    def write_data_row(self, dataset):
        for element in dataset:
            self.write_data_cell(self.current_row, element, dataset[element])
        self.current_row += 1

    def write_data_cell(self, row, column_name, data):
        self._worksheet.write(row, self.columns[column_name]['position'], data)

