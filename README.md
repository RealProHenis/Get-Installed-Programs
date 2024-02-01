## List of Installed Programs on Windows PCs
This simple Python script retrieves a list of installed programs from one or more Windows computers and writes those lists to text files.<br><br>
I created this program to have a backup list of every installed program for when I need to factory reset any of my Windows PCs

## Convert Python Script to Executable:
1. Install pyinstaller:
```
pip install pyinstaller
```
2. Open a terminal window in the same folder as `get-programs.py` and run this command:
*(include `--noconsole` if you want no console window to appear when running the executable)*
```
pyinstaller --onefile --noconsole get-programs.py
```
3. Run the compiled .exe file that gets created at `/dist/get-programs.exe`
