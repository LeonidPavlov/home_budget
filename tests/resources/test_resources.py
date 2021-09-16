import pytest
from genericpath import isdir, isfile

def test_existing_director() -> None:
    assert(isdir('resources'))

def test_existing_iso_files() -> None:
    assert(isfile('resources/entry.png'))

def test_existing_grc_resources_file() -> None:
    assert(isfile('resources/qrc_resources.py'))

