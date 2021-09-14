from PyQt5.QtWidgets import QApplication

from src.storage.storage import Storage
from src.view.main_view import MainView
from src.view.main import App


storage: Storage = Storage('databases', 'database.db')
try:
    if storage.create_directory():
        if storage.create_database_file():
            print('database created ...')
except Exception as err:
    print(err)

# app: MainView = MainView(storage)
App()

