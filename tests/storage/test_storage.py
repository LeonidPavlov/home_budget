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

def test_create_table_query() -> None:
    assert(storage.create_tables_query() == """
                        create table if not exists source_docs
                        (
                            entry_id integer primary key,
                            date text,
                            entry_type text,
                            bill_name text,
                            product text,
                            cost real,
                            amount real,
                            total real
                        );
        """)

def test_create_db_file_when_it_exist() -> None:
    assert(storage.create_database_file() == False)
    os.remove('test_db_dir/test_db.db')
    os.rmdir('test_db_dir')

