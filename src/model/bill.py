from enum import Enum


class BillType(Enum):
    active = 'active'
    passive = 'passive'


class Bill:
    def __init__(self,  article: str, bill_type: BillType) -> None:
        self._type = bill_type

