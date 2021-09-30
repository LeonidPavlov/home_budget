from enum import Enum
from datetime import datetime

class EntryType(Enum):
    debet_credit_plus = 'debet+ <-> credit+'
    debet_credit_minus = 'debet- <-> credit-'
    debet_debet = 'debet- <-> debet+'
    credit_credit = 'credit- <-> credit+'



class AccountingEntry:
    def __init__(self,  entry_id: int = 0,
                        date_time: datetime = datetime.now(),
                        entry_type: EntryType = EntryType.debet_debet,
                        bill_name: str = 'others',
                        source_leak_name: str = 'unknown',
                        product: str = 'product',
                        cost: float = 1.0,
                        amount: float = 1.0,
                        total: float = 1.0
                        ) -> None:
        self.date_time = date_time
        self.entry_type = entry_type
        self.bill_name = bill_name
        self.source_leak_name = source_leak_name
        self.product = product
        self.cost = cost
        self.amount = amount
        self.total = total
