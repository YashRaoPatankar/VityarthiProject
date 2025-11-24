# VityarthiProject
### Project Title  
**Simple Offline Habit Tracker**

### Overview of the Project  
A lightweight, fully offline habit tracking application built in pure Python. It helps you build good habits and break bad ones by tracking daily progress and maintaining streaks. All data is saved in a human-readable plain text file (`habitprogress.txt`) — no internet, no database, no extra setup needed.

### Features  
- Add good or bad habits  
- Log daily progress with simple yes/no  
- Automatic streak counter (resets if you skip a day)  
- Total successful days tracking  
- Special messages at 21-day and 66-day milestones  
- 100% offline — works anywhere  
- Data stored in editable plain text file  
- Input validation and duplicate protection  

### Technologies/Tools Used  
- Python 3 (standard library only)  
- Built-in modules: `os`, `datetime`  
- No external libraries or packages required  

### Steps to Install & Run the Project  
1. Make sure Python 3 is installed on your system  
2. Download or copy the `habit_tracker.py` file  
3. Open terminal/command prompt in the folder  
4. Run the program:  
   ```bash
   python habit_tracker.py
### Instructions for Testing
First run: No file exists → creates new progress automatically
Add a habit → quit → restart → check if it remembers
Log “yes” on multiple days (change system date or wait) → watch streak grow
Skip a day or answer “no” → streak resets
Try typing wrong inputs → program won’t crash
Open habitprogress.txt in Notepad → see your data in plain text (you can even edit it manually!)
### Output
<img width="666" height="769" alt="Screenshot 2025-11-24 at 7 19 18 PM" src="https://github.com/user-attachments/assets/4b789b1c-9e33-4ac6-a318-9374f4fb4f96" />
