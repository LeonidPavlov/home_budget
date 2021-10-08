from datetime import datetime
from functools import partial
from typing import Dict, Optional
from PyQt5.QtCore import QDateTime
from PyQt5.QtWidgets import QHBoxLayout, QLabel, QLayout, QMainWindow, QPushButton,\
                                 QVBoxLayout, QWidget
from PyQt5.QtGui import QKeyEvent, QMouseEvent
from PyQt5.QtCore import Qt

from src.view.chooser.calendar_pane import CalendarPane

class TimeRepresentation:
    def __init__(self, parent: QWidget, layout: QVBoxLayout, 
                                            format: Qt.DateFormat) -> None:
        self._parent = parent
        self._main_layout = layout
        self._format = format
        self._main_layout.addWidget(
            QLabel('choose time gap to selection from database'))
        self._layout = QHBoxLayout()
        self._setup_labels(self._layout)
        self._main_layout.addLayout(self._layout)

    def _setup_labels(self, layout: QHBoxLayout) -> None:
        layout.addWidget(QLabel('From'))
        self._begin_label = QLabel(QDateTime()\
                                    .currentDateTime().toString(self._format))
        self._begin_label.mousePressEvent = partial(self._open_calendar,
                            self._parent, self._begin_label)
        layout.addWidget(self._begin_label)
        label_to: QLabel = QLabel('To')
        label_to.setContentsMargins(20, 0, 5, 0)
        layout.addWidget(label_to)
        self._end_label: QLabel = QLabel(QDateTime()\
                                    .currentDateTime().toString(self._format))
        self._end_label.mousePressEvent = partial(self._open_calendar, 
                                            self._parent, self._end_label)
        layout.addWidget(self._end_label) 

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


class SelectionView(QWidget):
    def __init__(self, parent: QMainWindow, set_placeholder) -> None:
        super().__init__(parent=parent)
        self.set_placeholder = set_placeholder
        self._parent = parent
        self._layout: QVBoxLayout = QVBoxLayout()
        self._format: Qt.DateFormat = Qt.TextDate

        tr: TimeRepresentation = TimeRepresentation(self, 
                                        self._layout, self._format)

        self.setLayout(self._layout)
        self._parent.setCentralWidget(self)

    def print_begin(self) -> None:
        print(self.t.begin_time)
    
    def print_end(self) -> None:
        print(self.t.end_time)
