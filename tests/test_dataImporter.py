import pytest, os
from collections import OrderedDict
from viewer.data_importer import DataImporter

TEST_DATABASE_PATH = 'data_tests.db'


@pytest.fixture(scope="module")
def importer():
    yield DataImporter('../example_files/test.xls', TEST_DATABASE_PATH)
    os.remove(TEST_DATABASE_PATH)


class TestDataImporter(object):
    @pytest.fixture(autouse=True)
    def test_read_codes_from_excel(self, importer):
        codes = importer.read_codes_from_excel()
        except_result = OrderedDict([('Sheet1',
                                      [['Code', 'Description'], ['F1', 'Test 1'], ['F2', 'Test 2'], ['F3', 'Test 3'],
                                       ['F4', 'Test 4'], ['F5', 'Test 5'], ['F6', 'Test 6'], ['F7', 'Test 7'],
                                       ['F8', 'Test 8'], ['F9', 'Test 9'], ['F10', 'Test 10'], ['F11', 'Test 11'],
                                       ['F12', 'Test 12'], ['F13', 'Test 13'], ['F14', 'Test 14'], ['F15', 'Test 15'],
                                       ['F16', 'Test 16'], ['F17', 'Test 17'], ['F18', 'Test 18'], ['F19', 'Test 19'],
                                       ['F20', 'Test 20'], ['F21', 'Test 21'], ['F22', 'Test 22'], ['F23', 'Test 23'],
                                       ['F24', 'Test 24'], ['F25', 'Test 25'], ['F26', 'Test 26'], ['F27', 'Test 27'],
                                       ['F28', 'Test 28'], ['F29', 'Test 29'], ['F30', 'Test 30']])])
        assert codes == except_result

    def test_create_database_file(self, importer):
        is_database_created = importer.create_database_file()
        is_dbfile_exists = os.path.exists(TEST_DATABASE_PATH)
        assert is_database_created and is_dbfile_exists

    def test_add_codes_to_database(self, importer):
        assert True
