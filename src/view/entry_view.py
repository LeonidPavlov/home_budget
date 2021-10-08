from functools import partial
from PyQt5.QtGui import QDoubleValidator, QMouseEvent, QValidator
from typing import Dict, List
from PyQt5.QtCore import QDateTime, Qt
from PyQt5.QtWidgets import QComboBox, QFormLayout, QHBoxLayout, QLabel, \
    QLineEdit, QMainWindow, QPushButton, QVBoxLayout, \
    QWidget

from src.view.dialogs.alert import Achtung, AchtungType
from src.view.chooser.calendar_pane import CalendarPane
from src.storage.crud import Crud
from src.model.transaction import AccountingEntry, EntryType
from src.view.dialogs.confirmation import Confirmation


class Row:
    def __init__(self, title: str = '', content: List[str] = [],
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


class EntryView(QWidget):

    def __init__(self,  parent: QMainWindow = ..., 
                        entry: AccountingEntry = AccountingEntry(),
                        set_placeholder = None) -> None:
        super().__init__(parent = parent)
        self.entry = entry
        self.set_placeholder = set_placeholder
        self.parent: QMainWindow = parent
        self.main_layout: QVBoxLayout = QVBoxLayout()
        self.form_layout: QFormLayout = QFormLayout()
        self.h_layout: QHBoxLayout = QHBoxLayout()
        self._init_fields()
        self._add_buttons_panel()
        self.setLayout(self.main_layout)
        self.main_layout.addLayout(self.form_layout)
        self.main_layout.addLayout(self.h_layout)
        self.parent.setCentralWidget(self)

    def _init_fields(self) -> None:

        id_label: QLabel = Row('entry id : ', [str(self.entry.entry_id)],
                               self, self.form_layout).label_label()
        date_time: str = self.entry.date_time.toString(Qt.DefaultLocaleLongDate)
        self.date_time_label: QLabel = Row('date and time : ', [date_time],
                                self, self.form_layout).label_label()
        self.date_time_label.mousePressEvent = partial(
            self._open_calendar_view, self.date_time_label)

        items: List[str] = [EntryType.debet_debet.value,
                            EntryType.credit_credit.value,
                            EntryType.debet_credit_plus.value,
                            EntryType.debet_credit_minus.value]
        self.entry_type_combo: QComboBox = Row('entry type : ',
                                               items, self,
                                               self.form_layout). \
            label_combo()

        items = []  # to database
        self.bill_name_combo: QComboBox = Row('bill name : ', items,
                                              self, self.form_layout,
                                              editable=True).label_combo()

        items = []  # to database
        self.source_leak_name_combo: QComboBox = Row('source or leak name',
                                                     items, self,
                                                     self.form_layout,
                                                     editable=True).label_combo()

        items = []  # to database
        self.product_combo: QComboBox = Row('product : ', items, self,
                                            self.form_layout,
                                            editable=True).label_combo()

        nuber_validator: QValidator = QDoubleValidator()
        nuber_validator.setRange(0.0, 1e12, 2)

        tooltip_text: str = 'print number value\nand press Enter'
        
        items = [str(self.entry.cost)]
        self.cost_line: QLineEdit = Row('cost : ', items, self,
                                        self.form_layout,
                                        editable=True).label_editor()
        self.cost_line.setValidator(nuber_validator)
        self.cost_line.setText(str(self.entry.cost))
        self.cost_line.editingFinished.connect(partial(
            self._calculate, self.cost_line))
        self.cost_line.setToolTip(tooltip_text)

        items = [str(self.entry.amount)]
        self.amount_line: QLineEdit = Row('amount : ', items, self,
                                          self.form_layout,
                                          editable=True).label_editor()
        self.amount_line.setValidator(nuber_validator)
        self.amount_line.editingFinished.connect(partial(
            self._calculate, self.amount_line))
        self.amount_line.setToolTip(tooltip_text)

        items = [str(self.entry.total)]
        self.total_line: QLineEdit = Row('total : ', items, self,
                                         self.form_layout,
                                         editable=True).label_editor()
        self.total_line.setValidator(nuber_validator)
        self.total_line.editingFinished.connect(partial(
            self._calculate, self.total_line, False))
        self.total_line.setToolTip(tooltip_text)

    def _add_buttons_panel(self) -> None:
        buttons: Dict[str, QPushButton] = {
            'delete': QPushButton('&Delete'),
            'new': QPushButton('&New'),
            'update': QPushButton('&Update'),
            'cancel': QPushButton('&Cancel')
        }
        for b in buttons:
            self.h_layout.addWidget(buttons[b])

        if self.entry.entry_id == 0:
            buttons['delete'].setDisabled(True)
            buttons['update'].setDisabled(True)
        else:
            buttons['new'].setDisabled(True)

        buttons['cancel'].clicked.connect(self.close)
        buttons['cancel'].clicked.connect(self.set_placeholder)
        buttons['cancel'].clicked.connect(self.parent.resize)

        buttons['new'].clicked.connect(self._new_insertion)

    def set_date_time(self, dt: QDateTime, label: QLabel) -> None:
        self.entry.date_time = dt
        self.date_time_label.setText(dt.toString())

    def _open_calendar_view(self, label: QLabel, event: QMouseEvent) -> None:
        self.format: Qt.DateFormat = Qt.DefaultLocaleLongDate
        CalendarPane(self, self.date_time_label, self.format)

    def _validate_text_input(self) -> bool:
        self._validate_numbers()
        truth: bool = False
        if self.bill_name_combo.currentText() == '' or \
                self.source_leak_name_combo.currentText() == '' or \
                self.product_combo.currentText() == '':
            Achtung(self,
                'bill name,\n source leak field\n and product value\n must be not empty')
        else:
            truth = True
        return truth

    def _calculate(self, line: QLineEdit, straight_order: bool = True) -> None:
        self._validate_numbers()
        if straight_order:
            result: float = float(self.cost_line.text()) * \
                            float(self.amount_line.text())
            self.total_line.setText(str(result))
        else:
            result: float = float(self.total_line.text()) / \
                            float(self.amount_line.text())
            self.cost_line.setText(str(result))

    def _validate_numbers(self) -> None:
        lines = [self.cost_line, self.amount_line, self.total_line]
        for line in lines:
            if line.text().isascii() and line.text() != '' \
                    and line.text != '0' and line.text != '.':
                pass
            else:
                line.setText('1.0')

    def _new_insertion(self) -> None:
        entry: AccountingEntry = self._collect_entry_values_from_widget()
        self.entry = entry
        self._validate_numbers()
        if self._validate_text_input():
            Confirmation(self, self.insert_callback, entry=self.entry)

    def _collect_entry_values_from_widget(self) -> AccountingEntry:
        self._validate_numbers()
        entry: AccountingEntry = AccountingEntry(
            entry_id=self.entry.entry_id,
            date_time=self.entry.date_time.fromString(
                                self.date_time_label.text(), self.format),
            entry_type=self.entry.define_type_by_value( \
                            self.entry_type_combo.currentText()),
            bill_name=self.bill_name_combo.currentText(),
            source_leak_name=self.source_leak_name_combo.currentText(),
            product=self.product_combo.currentText(),
            cost=float(self.cost_line.text()),
            amount=float(self.amount_line.text()),
            total=float(self.total_line.text())
        )
        return entry

    def insert_callback(self, event) -> None:
        Crud(self.entry, self).insert_new()
    
    