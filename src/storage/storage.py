from genericpath import isdir, isfile
import os
import shutil
import sys
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
        if not isfile(self.file_name):
            file = sqlite3.connect(self.file_name)
            file.close()
            return True
        else:
            return False


