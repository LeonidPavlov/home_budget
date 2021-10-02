from enum import Enum
from typing import Dict, List
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QComboBox, QDialogButtonBox, QFormLayout, QGridLayout, QHBoxLayout, QLabel, QLayout, QMainWindow, QPushButton, QVBoxLayout,\
                            QWidget

from src.view.alert import Achtung
from src.storage.crud import Crud
from src.model.transaction import AccountingEntry, EntryType


class Row:
    def __init__(self,  title: str = '', content: List[str] = [], 
                parent: QWidget = ...,
                layout: QFormLayout = ...,
                editable: bool = False, width: int = 220) -> None:
        self.content: List[str] = content
        self.parent = parent
        self.layout: QFormLayout = layout
        self.editable: bool = editable
        self.width = width
        self.label: QLabel = QLabel(title)

    def label_label(self) -> QLabel:
        label: QLabel = QLabel(self.content[0])
        self.layout.addRow(self.label, label)
        self.layout.setAlignment(label, Qt.AlignRight)
        return label

    def label_combo(self) -> QComboBox:
        box: QComboBox = QComboBox(self.parent)
        box.addItems(self.content)
        box.setEditable(self.editable)
        box.setFixedWidth(self.width)
        self.layout.addRow(self.label, box)
        self.layout.setAlignment(box, Qt.AlignRight)
        return box

class EntryView:

    def __init__(self,  parent: QMainWindow, entry: AccountingEntry, 
                        crud: Crud) -> None:
        self.entry = entry
        self.widget : QWidget = QWidget(parent)
        self.parent: QMainWindow = parent
        self.main_layout: QVBoxLayout = QVBoxLayout()
        self.form_layout: QFormLayout  = QFormLayout()
        self.h_layout: QHBoxLayout = QHBoxLayout()
        self._init_fields()
        self._add_buttons_panel()
        self.widget.setLayout(self.main_layout)
        self.main_layout.addLayout(self.form_layout)
        self.main_layout.addLayout(self.h_layout)       
        self.parent.setCentralWidget(self.widget)

    def _init_fields(self) -> None:

        id_label: QLabel = Row('entry id : ', [str(self.entry.entry_id)],
                     self.widget, self.form_layout).label_label()         

        date_time: str = self.entry.date_time.strftime('%A %d %B  %H:%M %Y %Z')
        date_time_label: QLabel = Row('date and time : ',[date_time], 
                            self.widget,self.form_layout).label_label()

        items: List[str] = [  EntryType.debet_debet.value, 
                                EntryType.credit_credit.value,
                                EntryType.debet_credit_plus.value,
                                EntryType.debet_credit_minus.value]
        entry_type_combo: QComboBox = Row('entry type : ', 
                            items, self.widget, self.form_layout).\
                            label_combo()

        items = [] # to database
        bill_name_combo: QComboBox = Row('bill name : ', items, self.widget,
                        self.form_layout, editable=True).label_combo()
        
        items = [] # to database
        source_leak_name_combo: QComboBox = Row('soource or leak name', items, 
                    self.widget, self.form_layout, editable=True).label_combo()

        items = [] # to database
        product_combo: QComboBox = Row('product : ', items, self.widget, 
                    self.form_layout, editable=True).label_combo()

        items = [] #to database
        cost_combo: QComboBox = Row('cost : ', items, self.widget,
                            self.form_layout, editable=True).label_combo()

        items = [] #to database
        amount_combo: QComboBox = Row('amount : ', items, self.widget,
                            self.form_layout, editable=True).label_combo()

        items = [] #to database
        total_combo: QComboBox = Row('total : ', items, self.widget,
                            self.form_layout, editable=True).label_combo()

    def _add_buttons_panel(self) -> None:
        buttons: Dict[str, QPushButton] = {
            'delete' : QPushButton('&Delete'),
            'save'   : QPushButton('&Save'),
            'update' : QPushButton('&Update'),
            'cancel'   : QPushButton('&Cancel')
        }
        for b in buttons:
            self.h_layout.addWidget(buttons[b])

        if self.entry.entry_id is 0:
            buttons['delete'].setDisabled(True)
            buttons['update'].setDisabled(True)
        else:
            buttons['save'].setDisabled(True)
            
