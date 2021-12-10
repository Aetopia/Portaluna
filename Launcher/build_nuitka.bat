@echo off
py -OO -m nuitka --onefile --standalone --follow-imports --include-plugin-files=modules\launch.py --include-plugin-files=modules\config.py main.py --output-dir="%TEMP%" -o "Launch.exe"
timeout 5
