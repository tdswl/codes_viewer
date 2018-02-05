import pytest
import os
from viewer.database import DataBase


@pytest.fixture(scope="session")
def db(tmpdir_factory):
    db_path = "data_test.db"
    if os.path.exists(db_path):
        os.remove(db_path)
    yield DataBase(db_path)
    os.remove(db_path)

