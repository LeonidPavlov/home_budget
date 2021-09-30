from PyQt5.QtGui import QIcon, QKeySequence
from PyQt5.QtWidgets import QAction, QLabel, QMainWindow,\
                         QMenu, QMenuBar, QToolBar, QWidget
from PyQt5.QtCore import Qt
from functools import partial

import qrc.qrc_resources as res
from src.view.entry_view import EntryView
from src.storage.crud import Crud


class MainWindow(QMainWindow):
    def __init__(self, crud: Crud) -> None:
        super().__init__()
        self._crud: Crud = crud
        self.update_central_widget(QLabel('<h1>Ebumba</h1>'))
        self._add_menu_bar()
        

    def update_central_widget(self, widget: QWidget) -> None:
        # widget.setAlignment(Qt.AlignVCenter | Qt. AlignHCenter)
        self.setCentralWidget(widget)

    def _add_menu_bar(self) -> None:
        menu_bar: QMenuBar = QMenuBar(self)
        self._entry_menu = QMenu('&accounting entry', menu_bar)
        menu_bar.addMenu(self._entry_menu)
        self._add_entry_toolbar()
        self.setMenuBar(menu_bar)

    def _add_entry_toolbar(self) -> None:
        toolbar: QToolBar = QToolBar('accounting entry', self)
        
        new_action: QAction = QAction(QIcon(':entry'), 'new', self)
        new_action.setShortcut(QKeySequence.New)
        new_action.triggered.connect(self._setup_new_entry_widget)
        toolbar.addAction(new_action)
        self._entry_menu.addAction(new_action)
        
        self.addToolBar(Qt.LeftToolBarArea, toolbar)
        toolbar.setVisible(False)
        toolbar.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
    
    def _setup_new_entry_widget(self) -> None:
        view: EntryView = EntryView()
        self.setCentralWidget(view.instance())