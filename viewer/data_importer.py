import sqlite3
import pyexcel


class DataImporter:
    def __init__(self, excel_file_path, database_file_path):
        self.excel_file_path = excel_file_path
        self.database_file_path = database_file_path

    def read_codes_from_excel(self):
        spreadsheet = pyexcel.get_sheet(file_name=self.excel_file_path)
        codes = [tuple(row) for row in spreadsheet.rows()]  # prepare data for easy work in sqlite
        return codes

    def create_database_file(self):
        try:
            conn = sqlite3.connect(self.database_file_path)
            c = conn.cursor()
            # Create table
            c.execute('''CREATE TABLE IF NOT EXISTS codes
                                   (code TEXT NOT NULL PRIMARY KEY, description TEXT)''')
            # Save (commit) the changes
            conn.commit()
            # We can also close the connection if we are done with it.
            # Just be sure any changes have been committed or they will be lost.
            conn.close()
            return True
        except:
            return False

    def add_codes_to_database(self, codes_array):
        try:
            conn = sqlite3.connect(self.database_file_path)
            c = conn.cursor()
            c.executemany('INSERT INTO codes VALUES (?,?)', codes_array)
            conn.commit()
            conn.close()
            return True
        except:
            return False
