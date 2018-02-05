import pytest
import os


@pytest.mark.usefixtures("db")
class TestDataBase(object):
    @pytest.mark.first
    def test_create_database_file(self, db):
        is_database_created = db.create_database_file()
        is_dbfile_exists = os.path.exists(db.database_file_path)
        assert is_database_created and is_dbfile_exists

    @pytest.mark.run(after='test_create_database_file')
    def test_add_codes_to_database(self, db):
        except_result = [('test1', 'test1'), ('test2', 'test2')]
        is_added = db.add_codes_to_database(except_result)
        is_failed_to_add = db.add_codes_to_database([(12)])
        assert is_added and not is_failed_to_add

    @pytest.mark.run(after='test_add_codes_to_database')
    def test_get_codes(self, db):
        except_result = [('test1', 'test1'), ('test2', 'test2')]
        added_codes = db.get_codes()
        assert added_codes == except_result

    @pytest.mark.run(after='test_add_codes_to_database')
    def test_read_code_info_by_code(self, db):
        except_result = [('test1', 'test1'), ('test2', 'test2')]
        code_one = db.read_code_info_by_code('test1')
        code_two = db.read_code_info_by_code('test2')
        assert code_one == except_result[0] and code_two == except_result[1]

    @pytest.mark.run(after='test_add_codes_to_database')
    def test_search_code_by_string(self, db):
        except_result = [('test1', 'test1'), ('test2', 'test2')]
        search_one = db.search_code_by_string('te')
        search_two = db.search_code_by_string('test1')
        search_three = db.search_code_by_string('testdsfg')
        assert search_one == except_result and search_two[0] == except_result[0] and search_three == []

    @pytest.mark.last
    def test_remove_code(self, db):
        is_removed = db.remove_code('test1') and db.remove_code('test2')
        is_failed_to_remove = db.remove_code([])
        assert is_removed and not is_failed_to_remove
