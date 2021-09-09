from genericpath import isdir, isfile
import os
import sqlite3


class Storage:

    def __init__(self,  database_direcory_name: str = 'databases',
                        database_file_name: str = 'data.db') -> None:
        self.database_directory_name = database_direcory_name
        self.file_name = database_direcory_name + '/' + database_file_name
        
    def create_directory(self) -> bool:
        if not isdir(self.database_directory_name):
            os.mkdir(self.database_directory_name)
            return True
        else:
            return False

    def create_database_file(self) -> bool:
        truth: bool = False
        try:    
            if not isfile(self.file_name):
                file = sqlite3.connect(self.file_name)
                file.execute(self.create_tables_query())
                file.close()
                truth = True
            else:
                truth = False
        except sqlite3.OperationalError as err:
            print('SQLITE ERROR')
        return truth

    def create_tables_query(self) -> str:
        query: str = """
                        create table if not exists source_docs
                        (
                            id integer primary key,
                            date text,
                            entry_type text,
                            bill_name text,
                            product text,
                            cost real,
                            amount real,
                            total real
                        );
        """
        return query

