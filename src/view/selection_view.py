from functools import partial
from typing import List, Tuple
from PyQt5.QtCore import QDateTime
from PyQt5.QtWidgets import QButtonGroup, QCheckBox, QHBoxLayout, QLabel, \
    QMainWindow, QPushButton, QVBoxLayout, QWidget
from PyQt5.QtGui import QMouseEvent
from PyQt5.QtCore import Qt

from src.view.chooser.calendar_pane import CalendarPane
from src.storage.selection import Selection


class TimeRepresentation:
    def __init__(self, parent: QWidget, layout: QVBoxLayout,
                 format: Qt.DateFormat) -> None:
        self._parent = parent
        self._main_layout = layout
        self._format = format

        self.selection = Selection(self._parent)
        self.search_result: List[Tuple[int]] = []

        self._main_layout.addWidget(
            QLabel('choose time gap to selection from database'))

        self._setup_all_selection()

        self._layout = QHBoxLayout()
        self._setup_time_labels(self._layout)
        self._main_layout.addLayout(self._layout)

        self._button_group: QButtonGroup = QButtonGroup(self._parent)
        self._button_group.addButton(self._check_all)
        self._button_group.addButton(self._check_date)

    def _setup_all_selection(self) -> None:
        all_layout = QHBoxLayout()
        all_layout.addWidget(QLabel('All'))
        self._check_all: QCheckBox = QCheckBox(self._parent)
        self._check_all.stateChanged.connect(self.selection_from_db)
        all_layout.addWidget(self._check_all)
        self._button_all: QPushButton = QPushButton(self._parent)
        self._button_all.setVisible(False)
        all_layout.addWidget(self._button_all)
        self._main_layout.addLayout(all_layout)

    def selection_from_db(self) -> None:
        if self._check_all.isChecked():
            self.search_result = self.selection.selection_all_id()
            self._button_all.setText(str(len(self.search_result)) + ' items')
            self._button_all.setVisible(True)
            self._button_timegap.setVisible(False)
        if self._check_date.isChecked():
            self.search_result = self.selection. \
                select_id_by_time_gap(
                self.date_time_from_label(self.begin_label()),
                self.date_time_from_label(self.end_label()))
            self._button_timegap.setText(
                str(len(self.search_result)) + ' items')
            self._button_timegap.setVisible(True)
            self._button_all.setVisible(False)

    def _setup_time_labels(self, layout: QHBoxLayout) -> None:
        layout.addWidget(QLabel('From'))
        self._begin_label = QLabel(QDateTime()
                                   .currentDateTime().toString(self._format))
        self._begin_label.mousePressEvent = partial(self._open_calendar,
                                                    self._parent,
                                                    self._begin_label)
        layout.addWidget(self._begin_label)
        label_to: QLabel = QLabel('To')
        label_to.setContentsMargins(20, 0, 5, 0)
        layout.addWidget(label_to)
        self._end_label: QLabel = QLabel(QDateTime()
                                    .currentDateTime().toString(self._format))
        self._end_label.mousePressEvent = partial(self._open_calendar,
                                                  self._parent, self._end_label)
        layout.addWidget(self._end_label)
        self._check_date: QCheckBox = QCheckBox(self._parent)
        self._check_date.stateChanged.connect(self.selection_from_db)
        self._button_timegap: QPushButton = QPushButton(self._parent)
        self._button_timegap.setVisible(False)
        layout.addWidget(self._check_date)
        layout.addWidget(self._button_timegap)

    def begin_label(self) -> QLabel:
        return self._begin_label

    def end_label(self) -> QLabel:
        return self._end_label

    def date_time_from_label(self, label: QLabel) -> QDateTime:
        datetime: QDateTime = QDateTime().fromString(label.text(), self._format)
        return datetime

    def _open_calendar(self, parent: QWidget, target: QLabel,
                       event: QMouseEvent) -> None:
        CalendarPane(parent, target, self._format)


class StringFieldRepresentation:
    def __init__(self, parent: QWidget, layout: QVBoxLayout) -> None:
        pass


class SelectionView(QWidget):
    def __init__(self, parent: QMainWindow, set_placeholder) -> None:
        super().__init__(parent=parent)
        self.set_placeholder = set_placeholder
        self._parent = parent
        self._layout: QVBoxLayout = QVBoxLayout()
        self._format: Qt.DateFormat = Qt.SystemLocaleShortDate

        tr: TimeRepresentation = TimeRepresentation(self,
                                                    self._layout, self._format)

        self.setLayout(self._layout)
        self._parent.setCentralWidget(self)

    def print_begin(self) -> None:
        print(self.t.begin_time)

    def print_end(self) -> None:
        print(self.t.end_time)
