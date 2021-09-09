from enum import Enum


class BillType(Enum):
    active = 'active'
    passive = 'passive'


class Bill:
    def __init__(self,  article: str, type: BillType) -> None:
        self.__type = type

