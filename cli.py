import sys
from PyQt5.QtWidgets import QApplication

from src.storage.storage import Storage
from src.view.main_window import MainWindow
from src.storage.crud import Crud


storage: Storage = Storage()
try:
    if storage.create_directory():
        if storage.create_database_file():
            print('database created ...')
except Exception as err:
    print(err)

try:
    app: QApplication = QApplication([])
    mv: MainWindow = MainWindow()
    Crud(mv, storage)
    mv.show()
    sys.exit(app.exec())
except RuntimeError as err:
    print(err)
