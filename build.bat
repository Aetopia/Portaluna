@echo off
py -OO -m nuitka --onefile --standalone --follow-imports main.py --output-dir="%TEMP%" -o "execute.exe"
timeout 5
