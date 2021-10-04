import functools
from PyQt5.QtGui import QDoubleValidator, QMouseEvent, QValidator
from typing import Dict, List
from PyQt5.QtCore import QDateTime, Qt
from PyQt5.QtWidgets import QComboBox, QFormLayout, QHBoxLayout, QLabel, QLineEdit,\
            QMainWindow, QPushButton, QTextEdit, QVBoxLayout, QWidget

from src.view.alert import Achtung, AchtungType
from src.view.chooser.calendar_pane import CalendarPane
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
    
    def label_editor(self) -> QLineEdit:
        edit: QLineEdit = QLineEdit(self.content[0])
        edit.setFixedWidth(self.width)
        edit.setClearButtonEnabled(True)
        self.layout.addRow(self.label, edit)
        self.layout.setAlignment(edit, Qt.AlignRight)
        return edit

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

        date_time: str = self.entry.date_time.toString()
        self.date_time_label: QLabel = Row('date and time : ',[date_time], 
                            self.widget,self.form_layout).label_label()
        self.date_time_label.mousePressEvent = functools.partial(
                                self._open_calendar_view, self.date_time_label)


        items: List[str] = [  EntryType.debet_debet.value, 
                                EntryType.credit_credit.value,
                                EntryType.debet_credit_plus.value,
                                EntryType.debet_credit_minus.value]
        self.entry_type_combo: QComboBox = Row('entry type : ', 
                            items, self.widget, self.form_layout).\
                            label_combo()

        items = [] # to database
        self.bill_name_combo: QComboBox = Row('bill name : ', items, self.widget,
                        self.form_layout, editable=True).label_combo()
        

        items = [] # to database
        self.source_leak_name_combo: QComboBox = Row('soource or leak name',
                    items, self.widget, self.form_layout, 
                    editable=True).label_combo()

        items = [] # to database
        self.product_combo: QComboBox = Row('product : ', items, self.widget, 
                    self.form_layout, editable=True).label_combo()

        nuber_validator: QValidator = QDoubleValidator()
        nuber_validator.setRange(0.0, 1e12, 2)

        items = [str(self.entry.cost)]
        self.cost_line: QLineEdit = Row('cost : ', items, self.widget,
                            self.form_layout, editable=True).label_editor()
        self.cost_line.setValidator(nuber_validator)
        self.cost_line.setText(str(self.entry.cost))

        items = [str(self.entry.amount)] 
        self.amount_line: QLineEdit = Row('amount : ', items, self.widget,
                            self.form_layout, editable=True).label_editor()
        self.amount_line.setValidator(nuber_validator)

        items = [str(self.entry.total)]
        self.total_line: QLineEdit = Row('total : ', items , self.widget,
                            self.form_layout, editable=True).label_editor()
        self.total_line.setValidator(nuber_validator)

    def _add_buttons_panel(self) -> None:
        buttons: Dict[str, QPushButton] = {
            'delete' : QPushButton('&Delete'),
            'save'   : QPushButton('&Save'),
            'update' : QPushButton('&Update'),
            'cancel'   : QPushButton('&Cancel')
        }
        for b in buttons:
            self.h_layout.addWidget(buttons[b])

        if self.entry.entry_id == 0:
            buttons['delete'].setDisabled(True)
            buttons['update'].setDisabled(True)
        else:
            buttons['save'].setDisabled(True)
            
        buttons['save'].clicked.connect(self.validate_and_insert_to_db)
        buttons['cancel'].clicked.connect(self.widget.close)

    def set_date_time_from_entry(self, dt: QDateTime) -> None:
        self.entry.date_time = dt       
        self.date_time_label.setText(dt.toString())

    def _open_calendar_view(self, label: QLabel, event: QMouseEvent) -> None:
        CalendarPane(self.widget, self)

    def validate_and_insert_to_db(self) -> None:
        if  self.bill_name_combo.currentText() == '' or \
            self.source_leak_name_combo.currentText() == '' or\
            self.product_combo.currentText() == '':
            Achtung(self.widget, 
            'bill name, source leak field and\nproduct value must be not empty')

    def calculation(self, event) -> None:
        print ("ebites samei")