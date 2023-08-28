@echo off
setlocal

cd %~dp0
if not exist venv (
    python -m venv venv
)
call venv\Scripts\activate
git reset --hard HEAD
git pull

endlocal
