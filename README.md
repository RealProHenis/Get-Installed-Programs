## List of Installed Programs on Windows PCs
This simple Python script retrieves a list of installed programs from one or more Windows computers on your local network and writes those lists to text files.<br><br>
I created this program to have a backup list of every installed program for when I need to factory reset any of my Windows PCs

## How to run:
1. Open `get-programs.py` in a text editor & set the name of the PCs:
```
... existing code ...

computers = ["DESKTOP-1, DESKTOP-2"] # Replace with the name(s) of your Windows PCs

... existing code ...
```
2. Open `run.bat` and enjoy!

## Automatically run this program:
You can use Windows Task Scheduler to run this program at a time or interval of your choice.<br>
In order to do this, you must convert the python script into a single executeable file:

1. Install pyinstaller:
```
pip install pyinstaller
```
2. Open a terminal window in the same folder as `get-programs.py` and run this command:
*(include `--noconsole` if you want no console window to appear when running the executable)*
```
pyinstaller --onefile --noconsole get-programs.py
```
3. Run the compiled .exe file that gets created at `/dist/get-programs.exe`<br>
**NOTE:** Windows Security false flagged my compiled .exe as a virus, so I needed to add an exclusion for it. [Learn more](https://support.microsoft.com/en-us/windows/add-an-exclusion-to-windows-security-811816c0-4dfd-af4a-47e4-c301afe13b26)
5. Open Windows Task Scheduler.
    - In the Actions pane on the right, click on "Create Basic Task...".
    - Name the task (e.g., "Get-Installed-Programs").
    - Choose a trigger interval (e.g., Daily, Weekly, Monthly, etc.)
    - Choose a specific interval (e.g., time of day, day of the week, etc.)
    - Select "Start a program" as the Action
    - Browse to the location of the `get-programs.exe` you compiled using pyinstaller
    - You're all set! Click Finish.
