import sys
from typing import Type
from PyQt5.QtGui import QKeyEvent, QKeySequence
from PyQt5.QtWidgets import QLabel, QPushButton, QTimeEdit, QVBoxLayout,\
                            QWidget, QCalendarWidget, QHBoxLayout
from PyQt5.QtCore import QTime, QTimer, Qt
from datetime import datetime as dt
from PyQt5 import QtGui


class CalendarPane(QWidget):
    """
        it is a popup view to choose date and time and return 
        value back
        contents:
        - header label with date and going clock
        - calendar view
        - time editor
        - confirmation buttons
    """

    def __init__(self) -> None:
        super().__init__()
        self.__set_root_layout()
        self.__set_label_with_date_and_going_clock()
        self.__set_calendar_view()
        self.__set_time_editor()
        self.__set_navigation()
        self.__set_close_on_escape()
        self.setLayout(self.__main_vbox)
        self.show()

    def __set_root_layout(self) -> None:
        """ set main layout as a QVBoxLayout """
        self.__main_vbox: QVBoxLayout = QVBoxLayout(self)
        self.setLayout(self.__main_vbox)

    def __set_label_with_date_and_going_clock(self) -> None:
        """ set a going clock and date in header"""
        self.__clock_label: QLabel = QLabel()
        self.__set_content_into_label_clock()
        timer: QTimer = QTimer(self)
        timer.timeout.connect(self.__set_content_into_label_clock)
        timer.start(1000)
        self.__main_vbox.addWidget(self.__clock_label)

    def __set_content_into_label_clock(self) -> None:
        """ set content in clock label with format string """
        text: str = dt.now().strftime('%A  %d %B  %H:%M:%S  %Y')
        self.__clock_label.setText(text)
    
    def __set_calendar_view(self) -> None:
        """ set calendar view in vbox """
        self.__calendar = QCalendarWidget(self)
        self.__main_vbox.addWidget(self.__calendar)

    def __set_time_editor(self) -> None:
        """ set time editor with time-now start value"""
        label = QLabel('edit time with arrows -> ')
        time: QTime = QTime().currentTime() 
        self.__time_editor = QTimeEdit(self)
        self.__time_editor.setTime(time)
        self.__time_editor.setAlignment(Qt.AlignCenter)
        hbox: QHBoxLayout = QHBoxLayout()
        hbox.addWidget(label)
        hbox.addWidget(self.__time_editor)
        self.__main_vbox.addLayout(hbox)

    def __set_navigation(self) -> None:
        """navigation buttons confirm and cancel"""
        confirm: QPushButton = QPushButton(self)
        confirm.setText('confirm')
        confirm.clicked.connect(self.__result)
        cancel: QPushButton = QPushButton(self)
        cancel.setText('cancel')
        cancel.clicked.connect(self.close)
        hbox = QHBoxLayout()
        hbox.addWidget(confirm)
        hbox.addWidget(cancel)
        self.__main_vbox.addLayout(hbox)
    
    def __result(self) -> None:
        """temporary only prints values """
        print(str(self.__time_editor.time()))
        print(str(self.__calendar.selectedDate()))
        self.close()

    def __set_close_on_escape(self) -> None:
        pass

    def keyPressEvent(self, event1: QtGui.QKeyEvent) -> None:
        if event1.key() == Qt.Key_Escape:
            self.close()
