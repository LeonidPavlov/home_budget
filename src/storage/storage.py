import os
import sqlite3
from genericpath import isdir, isfile
from sqlite3 import Connection, connect, Cursor
from enum import Enum

from PyQt5.QtWidgets import QWidget

from src.view.dialogs.alert import Achtung, AchtungType


class DatabaseAndColumnsName(Enum):
    table_name = 'source_docs'
    entry_id = 'entry_id'
    date = 'date'
    entry_type = 'entry_type'
    bill_name = 'bill_name'
    product = 'product'
    cost = 'cost'
    amount = 'amount'
    total = 'total'


class Storage:
    def __init__(self,  database_direcory_name: str = 'data',
                        database_file_name: str = 'data.db') -> None:
        self.database_directory_name = database_direcory_name
        self.file_name = database_direcory_name + '/' + database_file_name
        
    def create_directory(self) -> bool:
        result: bool = False
        try:
            if not isdir(self.database_directory_name):
                os.mkdir(self.database_directory_name)
                result = True
        except (FileExistsError) as err:
            Achtung(None, err.__str__(), AchtungType.error, 
                    'create directory function', __file__ )
        return result

    def create_database_file(self) -> bool:
        conn: Connection 
        truth: bool = False
        try:
            conn = connect(self.file_name)
            cursor: Cursor = conn.cursor()
            cursor.execute(self.create_tables_query())
            conn.commit()
            cursor.close()
            truth = True
        except sqlite3.Error as err:
            Achtung(None, err.__str__(), AchtungType.error, 
                    'crate database file', __file__ )
            truth = False
        finally:
            if conn:
                conn.close()
            return truth

    def create_tables_query(self) -> str:
        d = DatabaseAndColumnsName
        query: str = f"""
                        create table if not exists {d.table_name.value}
                        (
                            {d.entry_id.value} integer primary key,
                            {d.date.value} text,
                            {d.entry_type.value} text,
                            {d.bill_name.value} text,
                            {d.product.value} text,
                            {d.cost.value} real,
                            {d.amount.value} real,
                            {d.total.value} real
                        );
        """
        return query
