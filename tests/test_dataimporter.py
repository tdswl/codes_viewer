import pytest
from viewer.data_importer import DataImporter


@pytest.fixture(scope="module")
def importer():
    return DataImporter('../example_files/test.xls')


@pytest.mark.usefixtures("importer", "db")
class TestDataImporter(object):
    def test_read_codes_from_excel(self, importer):
        codes = importer.read_codes_from_excel()
        except_result = [('Code', 'Description'), ('F1', 'Test 1'), ('F2', 'Test 2'), ('F3', 'Test 3'),
                         ('F4', 'Test 4'),
                         ('F5', 'Test 5'), ('F6', 'Test 6'), ('F7', 'Test 7'), ('F8', 'Test 8'), ('F9', 'Test 9'),
                         ('F10', 'Test 10'), ('F11', 'Test 11'), ('F12', 'Test 12'), ('F13', 'Test 13'),
                         ('F14', 'Test 14'), ('F15', 'Test 15'), ('F16', 'Test 16'), ('F17', 'Test 17'),
                         ('F18', 'Test 18'), ('F19', 'Test 19'), ('F20', 'Test 20'), ('F21', 'Test 21'),
                         ('F22', 'Test 22'), ('F23', 'Test 23'), ('F24', 'Test 24'), ('F25', 'Test 25'),
                         ('F26', 'Test 26'), ('F27', 'Test 27'), ('F28', 'Test 28'), ('F29', 'Test 29'),
                         ('F30', 'Test 30')]
        assert codes == except_result

    @pytest.mark.run(after='read_codes_from_excel')
    def test_import_from_excel_to_database(self, importer, db):
        is_imported = importer.import_from_excel_to_database(db)
        added_data = db.get_codes()

        except_result = [('F1', 'Test 1'), ('F2', 'Test 2'), ('F3', 'Test 3'),
                         ('F4', 'Test 4'),
                         ('F5', 'Test 5'), ('F6', 'Test 6'), ('F7', 'Test 7'), ('F8', 'Test 8'), ('F9', 'Test 9'),
                         ('F10', 'Test 10'), ('F11', 'Test 11'), ('F12', 'Test 12'), ('F13', 'Test 13'),
                         ('F14', 'Test 14'), ('F15', 'Test 15'), ('F16', 'Test 16'), ('F17', 'Test 17'),
                         ('F18', 'Test 18'), ('F19', 'Test 19'), ('F20', 'Test 20'), ('F21', 'Test 21'),
                         ('F22', 'Test 22'), ('F23', 'Test 23'), ('F24', 'Test 24'), ('F25', 'Test 25'),
                         ('F26', 'Test 26'), ('F27', 'Test 27'), ('F28', 'Test 28'), ('F29', 'Test 29'),
                         ('F30', 'Test 30')]

        assert is_imported and added_data == except_result
