@echo off
py -OO -m nuitka --onefile --standalone --follow-imports --include-plugin-files=install.py main.py --output-dir="%TEMP%" -o "MCFilesInstaller.exe"
timeout 5
