import sys
from PyQt5.QtWidgets import QApplication

from src.view.dialogs.alert import Achtung, AchtungType
from src.storage.storage import Storage
from src.view.main_window import MainWindow

storage: Storage = Storage()
try:
    if storage.create_directory():
        if storage.create_database_file():
            print('database created ...')
except Exception as err:
    Achtung(None, err.__str__(), AchtungType.error,
            'create storage instance', __file__)

try:
    app: QApplication = QApplication([])
    mv: MainWindow = MainWindow()
    mv.show()
    sys.exit(app.exec())
except Exception as err:
    Achtung(None, err.__str__(), AchtungType.error,
            'start application', __file__, )
