# List of Installed Programs on Windows PCs
This simple Python script retrieves a list of installed programs from one or more Windows computers on your local network and writes those lists to text files.<br><br>
I created this program to have a convenient backup list of every installed program on all of my Windows PCs for when I need to perform factory resets

## Requirements:
- Install [Python](https://www.python.org/downloads/)

## How to run:
1. Open `get-programs.py` in a text editor & set the name of the PCs:
```
... existing code ...

computers = ["DESKTOP-1, DESKTOP-2"] # Replace with the name(s) of your target Windows PCs

... existing code ...
```
2. Each target computer must have the Remote Registry service running<br>
- Open Windows Services and start the RemoteRegistry service <br>
*(optional: set the service to start automatically at startup if you're going to be running this program frequently)* <br><br>
**IMPORTANT:** Configure your Windows Firewall inbound rules to only accept Remote Service Management from the local IP address of the computer that will be running this code<br><br>
4. Open `run.bat` and enjoy!

## Automatically run this program:
You can automatically run this program at a specific time or interval of your choice.<br>

1. Open Windows Task Scheduler.
2. In the Actions pane on the right, click on "Create Basic Task...".
3. Name the task (e.g., "Get-Installed-Programs").
4. Choose a trigger interval (e.g., Daily, Weekly, Monthly, etc.)
5. Choose a specific interval (e.g., time of day, day of the week, etc.)
6. Select "Start a program" as the Action
7. Browse to the location of the `run.bat` that's located in the same folder as `get-programs.py`
8. Set the `Start in (optional):` location to the folder that contains `run.bat` & `get-programs.py` (e.g., "C:\Users\Henry\Documents\List-Of-Installed-Programs\").
9. You're all set! Click Finish.
