import pytest
from viewer.data_importer import DataImporter
from viewer.database import Code


@pytest.fixture(scope="module")
def importer():
    return DataImporter('../example_files/test.xls')


@pytest.mark.usefixtures("importer", "db")
class TestDataImporter(object):
    def test_read_codes_from_excel(self, importer):
        codes = importer.read_codes_from_excel()
        except_result = [Code('Code', 'Description'), Code('F1', 'Test 1'), Code('F2', 'Test 2'), Code('F3', 'Test 3'),
                         Code('F4', 'Test 4'), Code('F5', 'Test 5'), Code('F6', 'Test 6'), Code('F7', 'Test 7'),
                         Code('F8', 'Test 8'),
                         Code('F9', 'Test 9'), Code('F10', 'Test 10'), Code('F11', 'Test 11'), Code('F12', 'Test 12'),
                         Code('F13', 'Test 13'),
                         Code('F14', 'Test 14'), Code('F15', 'Test 15'), Code('F16', 'Test 16'), Code('F17', 'Test 17'),
                         Code('F18', 'Test 18'), Code('F19', 'Test 19'), Code('F20', 'Test 20'), Code('F21', 'Test 21'),
                         Code('F22', 'Test 22'), Code('F23', 'Test 23'), Code('F24', 'Test 24'), Code('F25', 'Test 25'),
                         Code('F26', 'Test 26'), Code('F27', 'Test 27'), Code('F28', 'Test 28'), Code('F29', 'Test 29'),
                         Code('F30', 'Test 30')]
        assert codes == except_result

    @pytest.mark.run(after='read_codes_from_excel')
    def test_import_from_excel_to_database(self, importer, db):
        is_imported = importer.import_from_excel_to_database(db)
        added_data = db.get_codes()

        except_result = [Code('F1', 'Test 1'), Code('F2', 'Test 2'), Code('F3', 'Test 3'), Code('F4', 'Test 4'),
                         Code('F5', 'Test 5'), Code('F6', 'Test 6'), Code('F7', 'Test 7'), Code('F8', 'Test 8'),
                         Code('F9', 'Test 9'), Code('F10', 'Test 10'), Code('F11', 'Test 11'), Code('F12', 'Test 12'),
                         Code('F13', 'Test 13'), Code('F14', 'Test 14'), Code('F15', 'Test 15'), Code('F16', 'Test 16'),
                         Code('F17', 'Test 17'), Code('F18', 'Test 18'), Code('F19', 'Test 19'), Code('F20', 'Test 20'),
                         Code('F21', 'Test 21'), Code('F22', 'Test 22'), Code('F23', 'Test 23'), Code('F24', 'Test 24'),
                         Code('F25', 'Test 25'), Code('F26', 'Test 26'), Code('F27', 'Test 27'), Code('F28', 'Test 28'),
                         Code('F29', 'Test 29'), Code('F30', 'Test 30')]

        assert is_imported and added_data == except_result
