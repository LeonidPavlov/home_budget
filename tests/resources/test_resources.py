import pytest
from genericpath import isdir, isfile

def test_existing_director() -> None:
    assert(isdir('qrc'))

image_dir: str = 'qrc/images/'
def test_existing_entry_png() -> None:
    assert(isfile(image_dir + 'entry_64x64.png'))

def test_existing_edit_png() -> None:
    assert(isfile(image_dir + 'edit_64x64.png'))

def test_existing_search_png() -> None:
    assert(isfile(image_dir + '/search_64x64.png'))

def text_existing_source_qrc_File() -> None:
    assert(isfile('qrc/.qrc'))

def test_existing_grc_resources_file() -> None:
    assert(isfile('qrc/qrc_resources.py'))


