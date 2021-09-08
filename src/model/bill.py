from enum import Enum

class EntryType(Enum):
    debet_credit_plus = 'debet+ <-> credit+'
    debet_credit_minus = 'debet- <-> credit-'
    debet_debet = 'debet- <-> debet+'
    credit_credit = 'credit- <-> credit+'

class BillType(Enum):
    active = 'active'
    passive = 'passive'

class Bill:
    def __init__(self,  article: str, type: BillType) -> None:
        self.__type = type

