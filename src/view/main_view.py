from src.storage.storage import Storage
from PyQt5.QtWidgets import QApplication, QMainWindow, QMenuBar,\
                            QToolBar, QWidget, QLabel, QMenu
from PyQt5.QtCore import Qt, left
import sys

class MainView:
    storage: Storage

    def __init__(self, storage_instace: Storage) -> None:
        MainView.storage = storage_instace
        self.app: QApplication = QApplication(sys.argv)
        self._init_main_window_widget()
        self._create_menu_bar()
        self._create_tool_bars()
        self.add_central_widget(QLabel('<h1> Ebatushki </h1>'))
        self.window.show()
        sys.exit(self.app.exec_())

    def _init_main_window_widget(self) -> None:
        self.window: QMainWindow = QMainWindow()
        self.window.setWindowTitle('Home Budget')
        self.window.setGeometry(500, 300, 960, 540)
        print('init main window')


    def add_central_widget(self, widget: QWidget) -> None:
        self.window.centralWidget = widget
        self.window.centralWidget.setAlignment \
                            (Qt.AlignHCenter | Qt.AlignVCenter)
        self.window.setCentralWidget(widget)
        print('central widget')

    def _create_menu_bar(self) -> None:
        menu_bar: QMenuBar = QMenuBar()
        self.window.setMenuBar(menu_bar)
        print('create menu bar')
        fileMenu: QMenu = menu_bar.addMenu('New Entry')
        editMenu: QMenu = menu_bar.addMenu('EDIT')
        helpMenu = menu_bar.addMenu("&Help")

    def _create_tool_bars(self) -> None:
        top_tool_bar: QToolBar = QToolBar('EDIT', self.window)
        self.window.addToolBar(Qt.TopToolBarArea, top_tool_bar)
        left_tool_bar: QToolBar = QToolBar('ebat', self.window)
        self.window.addToolBar(Qt.LeftToolBarArea, left_tool_bar)
        right_tool_bar: QToolBar = QToolBar('ssat', self.window)
        self.window.addToolBar(Qt.RightToolBarArea, right_tool_bar)
