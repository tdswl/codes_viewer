import pyexcel


class DataImporter:
    def __init__(self, excel_file_path):
        self.excel_file_path = excel_file_path

    def read_codes_from_excel(self):
        spreadsheet = pyexcel.get_sheet(file_name=self.excel_file_path)
        codes = [tuple(row) for row in spreadsheet.rows()]  # prepare data for easy work in sqlite
        return codes

    def import_from_excel_to_database(self, db):
        codes = self.read_codes_from_excel()
        return db.add_codes_to_database(codes[1:])
