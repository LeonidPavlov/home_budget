#!/bin/bash -x

python3 -m venv venv

venv/bin/python -m pip install --upgrade pip setuptools wheel

pip=venv/bin/pip\ install\ --upgrade

$pip fbs pyqt5 
$pip pyinstaller 
$pip pytest

venv/bin/python -m pytest

rm -f dist/cli

venv/bin/pyinstaller cli.py --onefile

./dist/cli
