import sys
from enum import Enum
from typing import Optional
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QTextCharFormat
from PyQt5.QtWidgets import QApplication, QDialog, QDialogButtonBox, QLabel, QPlainTextDocumentLayout, QPlainTextEdit,\
                                QVBoxLayout, QWidget, QTextEdit


class AchtungType(Enum):
    message = 'message'
    error = 'error'


class Achtung:
    def __init__(self,  parent: Optional[QWidget], content: str = '', 
                        achtung_type: AchtungType = AchtungType.message,
                        context: str = '', file: str = '') -> None:
        self.content: str = f'{content}\n{context}\n{file}'   
        self.parent: Optional[QWidget] = parent
        self.achtung_type: AchtungType = achtung_type 
        if parent == None:
            self.app = QApplication([])
            self._create_dialog()
            sys.exit(self.app.exec())
        else:
            self.parent = parent
            self._create_dialog()

    def _create_dialog(self) -> None:
        self.dialog = QDialog(self.parent)
        omni: str = '''
                font-size: 16px;
                font-weight: bold;
            '''
        if self.achtung_type is AchtungType.error:
            self.dialog.setStyleSheet('''
                background-color: darkred;
                color: white;
            ''' + omni)
        if self.achtung_type is AchtungType.message:
            self.dialog.setStyleSheet('''
                background-color: purple;
                color: whitesmoke;
            ''' + omni)

        layout: QVBoxLayout = QVBoxLayout(self.dialog)

        text: QPlainTextEdit = QPlainTextEdit(self.content)
        text.setEnabled(False)
        layout.addWidget(text)
        layout.addWidget(text)

        btns: QDialogButtonBox = QDialogButtonBox(self.dialog)
        btns.setStandardButtons(QDialogButtonBox.Ok)
        btns.accepted.connect(self.dialog.close)      
        
        layout.addWidget(btns)
        self.dialog.setLayout(layout)
        self.dialog.setMinimumWidth(400)
        self.dialog.show()
