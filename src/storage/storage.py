import os
import sqlite3
from genericpath import isdir, isfile
from sqlite3 import Connection, connect
from enum import Enum


from src.view.alert import Achtung, AchtungType


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
        try:
            if not isdir(self.database_directory_name):
                os.mkdir(self.database_directory_name)
                return True
            else:
                return False
        except (FileExistsError) as err:
            Achtung(None, err.__str__(), AchtungType.error, 
                    'create directory method', __file__)

    def create_database_file(self) -> bool:
        truth: bool = False
        try:    
            if not isfile(self.file_name):
                conn: Connection = self.connect_with_db()
                self.execute_query(conn, self.create_tables_query())
                self.close_connection(conn)
                truth = True
            else:
                truth = False
        except sqlite3.Error as err:
            Achtung(None, err.__str__(), AchtungType.error, 
                    'create database file method', __file__)
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


    def connect_with_db(self) -> Connection:
        try:
            conn = connect(self.file_name)
            return conn
        except sqlite3.Error as err:
            Achtung(None, err.__str__(), AchtungType.error, 
                    'connect_with_db method', __file__)


    def execute_query(self, conn: Connection, query: str = '') -> None:
        try:
            conn.execute(query)
        except sqlite3.Error as err:
            Achtung(None, err.__str__(), AchtungType.error, 
                    'execute_querry method', __file__)

    
    def close_connection(self, conn: Connection) -> None:
        conn.close()
