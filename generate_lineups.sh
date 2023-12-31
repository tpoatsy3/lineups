#!/bin/bash
cd "$(dirname "$0")"
chmod 777 .
[ ! -d "./venv" ] && python3 -m venv venv
source venv/bin/activate
python3 -m pip install -r requirements.txt
python3 main.py