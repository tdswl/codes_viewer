import pytest
import os


@pytest.mark.usefixtures("db")
class TestDataBase(object):
    def test_create_database_file(self, db):
        is_database_created = db.create_database_file()
        is_dbfile_exists = os.path.exists(db.database_file_path)
        assert is_database_created and is_dbfile_exists

    @pytest.mark.run(after='test_create_database_file')
    def test_add_codes_to_database(self, db):
        except_result = [('test1', 'test1'), ('test2', 'test2')]
        is_added = db.add_codes_to_database(except_result)
        added_codes = db.get_codes()

        # cleanup
        is_removed = db.remove_code('test1') and db.remove_code('test2')

        assert is_added and added_codes == except_result and is_removed
