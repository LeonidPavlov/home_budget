import pytest
from datetime import datetime as dt

from src.model.transaction import AccountingEntry, EntryType


def test_entry_type_1() -> None:
    assert (EntryType.debet_credit_plus.value == '+ debet | + credit')


def test_entry_type_2() -> None:
    assert (EntryType.debet_credit_minus.value == '- debet | - credit')


def test_entry_type_3() -> None:
    assert (EntryType.debet_debet.value == '- debet | + debet')


def test_entry_type_4() -> None:
    assert (EntryType.credit_credit.value == '- credit | + credit')


ae: AccountingEntry = AccountingEntry()


def test_AccountingEntry_init() -> None:
    assert (ae != None)


def test_date_time() -> None:
    assert (ae.date_time.date().month()) == dt.now().month


def test_entry_type() -> None:
    assert (ae.entry_type == EntryType.debet_debet)


def test_bill_name() -> None:
    assert (ae.bill_name == 'others')


def test_source_leak_name() -> None:
    assert (ae.source_leak_name == 'unknown')


def test_product() -> None:
    assert (ae.product == 'product')


def test_cost_value() -> None:
    assert (ae.cost == 1.0)


def test_amount_value() -> None:
    assert (ae.amount == 1.0)


def test_total_value() -> None:
    assert (ae.total == 1.0)


def test_define_type_debet_credit_plus() -> None:
    ae.entry_type = EntryType.debet_credit_plus
    assert (AccountingEntry.define_type_by_value(
        '+ debet | + credit') == EntryType.debet_credit_plus)


def test_define_type_debet_credit_minus() -> None:
    ae.entry_type = EntryType.debet_credit_minus
    assert (AccountingEntry.define_type_by_value(
        '- debet | - credit') == EntryType.debet_credit_minus)


def test_define_type_debet_debet() -> None:
    ae.entry_type = EntryType.debet_debet
    assert (AccountingEntry.define_type_by_value(
        '- debet | + debet') == EntryType.debet_debet)


def test_define_type_credit_credit() -> None:
    ae.entry_type = EntryType.credit_credit
    assert (AccountingEntry.define_type_by_value(
        '- credit | + credit') == EntryType.credit_credit)
