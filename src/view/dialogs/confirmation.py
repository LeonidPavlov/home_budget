from typing import Optional
from PyQt5.QtWidgets import QDialog, QHBoxLayout, QPlainTextEdit, QPushButton, QVBoxLayout, QWidget

from src.model.transaction import AccountingEntry

class Confirmation(QDialog):
    def __init__(self,  parent: Optional[QWidget] = ...,
                        callback = ...,
                        text: str = "Confirm saving accounting entry:", 
                        entry: AccountingEntry = AccountingEntry()) -> None:
        super().__init__(parent=parent)
        self.text = text
        self.callback = callback
        self.entry = entry
        self.truth = False

        self.text_edit: QPlainTextEdit = QPlainTextEdit(self)
        self.filling_content()
        
        self.layout: QVBoxLayout = QVBoxLayout()
        self.layout.addWidget(self.text_edit)
        self.text_edit.setFixedWidth(400)
        self.text_edit.setEnabled(False)
        
        self.add_confirmatin_buttons()
        
        self.setStyleSheet( """
                                background-color: green;
                                color: whitesmoke;
                            """)
        self.setLayout(self.layout)
        self.show()


    def  filling_content(self) -> None:
        text: str = self.text + '\n'
        text = text +   'date -> ' + self.entry.date_time.toString() + '\n' +\
                        'entry type -> ' + self.entry.entry_type.value + '\n'\
                        'bill name -> ' + self.entry.bill_name + '\n' +\
                        'source or leak -> ' + self.entry.source_leak_name+'\n'\
                        'product -> ' + self.entry.product + '\n'\
                        'cost -> ' + str(self.entry.cost) + '\n'\
                        'amount -> ' + str(self.entry.amount) + '\n'\
                        'total -> ' + str(self.entry.total) + '\n'
        self.text_edit.setPlainText(text)

    def add_confirmatin_buttons(self) -> None:
        buttons_layout: QHBoxLayout = QHBoxLayout()
        
        ok: QPushButton = QPushButton('&Ok')
        ok.setFixedWidth(70)
        buttons_layout.addWidget(ok)
        ok.clicked.connect(self.confirmation)

        cancel: QPushButton = QPushButton('&Cancel')
        cancel.setFixedWidth(70)
        buttons_layout.addWidget(cancel)
        cancel.clicked.connect(self.close)

        self.layout.addLayout(buttons_layout)

    def confirmation(self, event) -> None:
        self.callback(event)
        self.close()
