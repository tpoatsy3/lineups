#!/bin/bash
cd "$(dirname "$0")"
[ ! -d "./venv" ] && python3 -m venv venv
source venv/bin/activate
git reset --hard HEAD
git pull
