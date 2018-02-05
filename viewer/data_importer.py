import sqlite3
import pyexcel


class DataImporter:
    def __init__(self, excel_file_path, database_file_path):
        self.excel_file_path = excel_file_path
        self.database_file_path = database_file_path

    def read_codes_from_excel(self):
        # TODO: create excel read function
        book_dict = pyexcel.get_book_dict(file_name=self.excel_file_path)
        return book_dict

    def create_database_file(self):
        # TODO: create database creation function
        return 0

    def add_codes_to_database(self, codes_dict):
        # TODO: create add codes function
        return 0
