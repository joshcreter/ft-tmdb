class Worksheet:
    _worksheet = ''
    columns = {}
    workbook = ''
    header_row = 0
    current_row = 1

    def __init__(self, workbook):
        self.workbook = workbook
        self.generate_worksheet()

    def write_header_cell(self, worksheet, column_position, column_data):
        header_format = self.workbook.add_format({'bg_color': 'green'})

        worksheet.write(self.header_row, column_position, column_data['label'], header_format)
        worksheet.set_column(column_position,  column_position,  column_data['width'])

    def generate_worksheet(self):
        worksheet = self.workbook.add_worksheet(self.name)

        column_position = 0
        for column_data in self.columns:
            self.write_header_cell(worksheet, column_position, self.columns[column_data])
            column_position += 1

        self._worksheet = worksheet

    def get_worksheet(self):
        return self

    def get_columns(self):
        return self.columns

    def write_data_row(self, dataset):
        column_position = 0
        # for element in dataset:
        #     self.write_data_cell(self.current_row, column_position, dataset[element])
        #     column_position += 1

        for column_data in self.columns:
            # print(column_data)
            data = dataset.get(column_data, None)
            if data:
                self.write_data_cell(self.current_row, column_position, dataset[column_data])
            column_position += 1

        # for element in dataset:
        #     self.write_data_cell(self.current_row, column_position, dataset[element])
        #     column_position += 1

        self.current_row += 1

    def write_data_cell(self, row, column, data):
        self._worksheet.write(row, column, data)

    # def write_data_cell(self, row, column_name, data):
    #     self._worksheet.write(row, self.columns[column_name]['position'], data)

