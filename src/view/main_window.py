from src.storage.storage import Storage
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
import sys

class MainWindow:
    storage: Storage

    def __init__(self, storage_instace: Storage) -> None:
        MainWindow.storage = storage_instace
        self.app = QApplication(sys.argv)
        window: QWidget = QWidget()
        window.setGeometry(500, 300, 500, 300)
        window.show()
        sys.exit(self.app.exec_())
