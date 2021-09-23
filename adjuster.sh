#!/bin/bash -x

python3 -m venv venv

venv/bin/python -m pip install --upgrade pip setuptools wheel

pip=venv/bin/pip\ install\ --upgrade

$pip fbs pyqt5 
$pip pyinstaller 
$pip pytest

qrc_dir=qrc
rm -f $qrc_dir/qrc_resources.py
venv/bin/pyrcc5 -o $qrc_dir/qrc_resources.py $qrc_dir/.qrc

venv/bin/python -m pytest
rm -f dist/cli

venv/bin/pyinstaller cli.py --onefile

./dist/cli
