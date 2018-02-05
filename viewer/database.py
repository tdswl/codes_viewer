import sqlite3


class DataBase:
    def __init__(self, database_file_path):
        self.database_file_path = database_file_path

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

    def get_codes(self):
        try:
            conn = sqlite3.connect(self.database_file_path)
            c = conn.cursor()
            added_data = [row for row in c.execute('SELECT * FROM codes')]
            conn.close()
            return added_data
        except:
            return None

    def remove_code(self, code):
        try:
            conn = sqlite3.connect(self.database_file_path)
            c = conn.cursor()
            c.execute('DELETE FROM codes WHERE code=?', (code,))
            conn.commit()
            conn.close()
            return True
        except:
            return False

    def read_code_info_by_code(self, code):
        try:
            conn = sqlite3.connect(self.database_file_path)
            c = conn.cursor()
            c.execute('SELECT * FROM codes WHERE code=?', (code,))
            result_code = c.fetchone()
            conn.close()
            return result_code
        except:
            return None

    def search_code_by_string(self, search_string):
        try:
            conn = sqlite3.connect(self.database_file_path)
            c = conn.cursor()
            codes = [row for row in c.execute('SELECT * FROM codes WHERE code LIKE ?', ('%' + search_string + '%',))]
            conn.close()
            return codes
        except:
            return None
