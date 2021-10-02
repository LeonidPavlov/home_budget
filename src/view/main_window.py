from PyQt5.QtGui import QIcon, QKeySequence
from PyQt5.QtWidgets import QAction, QLabel, QMainWindow,\
                         QMenu, QMenuBar, QToolBar, QWidget
from PyQt5.QtCore import QSize, Qt
from functools import partial

import qrc.qrc_resources as res
from src.view.entry_view import EntryView
from src.storage.crud import Crud
from src.model.transaction import AccountingEntry


class MainWindow(QMainWindow):
    def __init__(self, crud: Crud) -> None:
        super().__init__()
        self.crud: Crud = crud
        self.setCentralWidget(QLabel('<h1>PLACEHOLDER</h1>'))
        # self.setMinimumSize(640, 360)
        self._add_menu_bar()
        self.set_dev_style()

    def _add_menu_bar(self) -> None:
        menu_bar: QMenuBar = QMenuBar(self)
        self.entry_menu = QMenu('&accounting entry', menu_bar)
        menu_bar.addMenu(self.entry_menu)
        self._add_entry_toolbar()
        self.setMenuBar(menu_bar)

    def _add_entry_toolbar(self) -> None:
        toolbar: QToolBar = QToolBar('accounting entry', self)
        
        new_action: QAction = QAction(QIcon(':entry'), 'new', self)
        new_action.setShortcut(QKeySequence.New)
        new_action.triggered.\
                connect(partial(self._setup_entry_widget, AccountingEntry()))
        toolbar.addAction(new_action)
        self.entry_menu.addAction(new_action)
         
        self.addToolBar(Qt.LeftToolBarArea, toolbar)
        # toolbar.setVisible(False)
        toolbar.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
    
    def _setup_entry_widget(self, entry: AccountingEntry) -> None:
        EntryView(self, entry, self.crud)
    
    def set_dev_style(self) -> None:
        self.setStyleSheet('''
            background-color: bisque;
            color: navy;
            border-color: navy;
            font-size: 14px;
            font-weight: 900;
        ''')