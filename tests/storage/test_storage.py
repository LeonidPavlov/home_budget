from genericpath import isdir
import os

from src.storage.storage import Storage

storage = Storage('test_db_dir', 'test_db.db')

def test_create_directory_when_directory_absent() -> None:
    assert(storage.create_directory() == True)

def test_create_directory_when_directory_exist() -> None:
    assert(storage.create_directory() == False)

def test_create_db_file_when_it_not_exist() -> None:
    assert(storage.create_database_file() == True)

def test_create_db_file_when_it_exist() -> None:
    assert(storage.create_database_file() == False)
    os.remove('test_db_dir/test_db.db')
    os.rmdir('test_db_dir')

