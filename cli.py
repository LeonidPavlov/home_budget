import sys
from PyQt5.QtWidgets import QApplication, QWidget

from src.view.alert import Achtung, AchtungType
from src.storage.storage import Storage
from src.view.main_window import MainWindow
from src.storage.crud import Crud


storage: Storage = Storage()
try:
    if storage.create_directory():
        if storage.create_database_file():
            print('database created ...')
except Exception as err:
    Achtung(None, err.__str__(), AchtungType.error, 
            'storage create directory', __file__,)


try:
    app: QApplication = QApplication([])
    crud: Crud = Crud(storage)
    mv: MainWindow = MainWindow(crud=crud)
    mv.show()
    sys.exit(app.exec())
except Exception as err:
    Achtung(None, err.__str__(), AchtungType.error, 
            'start application', __file__,)
