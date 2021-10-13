from sqlite3 import Connection
from sqlite3 import Cursor, Error, connect
from PyQt5.QtWidgets import QWidget

from src.model.transaction import AccountingEntry
from src.storage.storage import DatabaseAndColumnsName, Storage
from src.view.dialogs.alert import Achtung


class Crud:
    n = DatabaseAndColumnsName

    def __init__(self, entry: AccountingEntry, parent: QWidget) -> None:
        self.entry = entry
        self.parent = parent
        self.storage = Storage()

    def insert_new(self) -> bool:
        truth: bool = False
        try:
            conn: Connection = connect(self.storage.file_name)
            cursor: Cursor = conn.cursor()
            query: str = f"""
                INSERT INTO {Crud.n.table_name.value} (
                    {Crud.n.datetime.value},
                    {Crud.n.year.value},
                    {Crud.n.month.value},
                    {Crud.n.day.value},
                    {Crud.n.hours.value},
                    {Crud.n.minutes.value},
                    {Crud.n.entry_type.value},
                    {Crud.n.bill_name.value},
                    {Crud.n.source.value},
                    {Crud.n.product.value},
                    {Crud.n.cost.value},
                    {Crud.n.amount.value},
                    {Crud.n.total.value}
                ) VALUES (
                    '{self.entry.date_time.toString()}',
                    {self.entry.date_time.date().year()},
                    {self.entry.date_time.date().month()},
                    {self.entry.date_time.date().day()},
                    {self.entry.date_time.time().hour()},
                    {self.entry.date_time.time().minute()},
                    '{self.entry.entry_type.value}',
                    '{self.entry.bill_name}',
                    '{self.entry.source_leak_name}',
                    '{self.entry.product}',
                    {self.entry.cost},
                    {self.entry.amount},
                    {self.entry.total}
                );
            """
            cursor.execute(query)
            conn.commit()
            cursor.close()
            truth = True
        except Error as err:
            print(err.__str__())
            truth = False
        finally:
            if conn:
                conn.close()
                Achtung(self.parent, 'entry added to database')
        return truth
