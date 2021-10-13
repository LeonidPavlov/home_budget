from sqlite3 import Connection, Error
from sqlite3 import Cursor, connect
from PyQt5.QtCore import QDateTime
from PyQt5.QtWidgets import QWidget

from src.view.dialogs.alert import Achtung, AchtungType
from src.storage.storage import Storage, DatabaseAndColumnsName
from typing import List, Tuple


class Selection:
    """
        contents any huynya vsyakaya
    """

    def __init__(self, parent: QWidget) -> None:
        self.parent = parent
        self.storage = Storage()
        self.file = self.storage.file_name

    def selection_all_id(self) -> List[Tuple[int]]:
        result: List[Tuple[int]] = []
        n = DatabaseAndColumnsName  # enum
        query: str = f'''
                        select {n.entry_id.value} from {n.table_name.value};
                        '''
        try:
            conn: Connection = connect(self.file)
            cursor: Cursor = conn.cursor()
            cursor.execute(query)
            result = cursor.fetchall()
            conn.commit()
            cursor.close()
        except Error as err:
            Achtung(self.parent, err.__str__(), AchtungType.error,
                    'method selection all id', __file__)
        finally:
            if conn:
                conn.close()
        return result

    def select_id_by_time_gap(self, start: QDateTime,
                              finish: QDateTime) -> List[Tuple[int]]:
        result: List[Tuple[int]] = []
        return result

        # datetime inserted from datatype
        #  need to refactor in idea because dont look normal
