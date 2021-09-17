import pytest
from genericpath import isdir, isfile

def test_existing_director() -> None:
    assert(isdir('resources'))

def test_existing_entry_png() -> None:
    assert(isfile('resources/entry.png'))

def test_existing_edit_png() -> None:
    assert(isfile('resources/edit.png'))

def test_existing_search_png() -> None:
    assert(isfile('resources/search.png'))

def test_existing_grc_resources_file() -> None:
    assert(isfile('resources/qrc_resources.py'))

