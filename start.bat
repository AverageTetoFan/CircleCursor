@echo off
cd /d "%~dp0"

call venv\Scripts\activate.bat

python cursor_visual.py

pause