# Music Bot Automation

## 📌 Project Overview
This Python script automates sending music commands to a Discord bot using `pyautogui`. It reads commands from `file1.txt` and types them into Discord, simulating manual input.

---

## 🗂 Project Structure
```
music-bot-discord/
│── main.py         # The script to send commands
│── file1.txt       # The text file with song commands
│── README.md       # Instructions for usage
```

---

## 🛠 Prerequisites
### 1️⃣ Install Python
Make sure Python is installed on your system. You can check by running:
```sh
python --version
```
If not installed, download it from [python.org](https://www.python.org/downloads/).

### 2️⃣ Install Required Module
You need `pyautogui` for automating key presses. Install it using:
```sh
pip install pyautogui
```

---

## 🚀 How to Use
### **Step 1: Prepare `file1.txt`**
- Add song commands to `file1.txt`, each on a new line.
- Example:
  ```
  m!play Skechers by DripReport
  m!play Blinding Lights by The Weeknd
  ```

### **Step 2: Open Discord**
- Open Discord and navigate to the chat where you want to send commands.

### **Step 3: Run the Script**
- Open VS Code and navigate to the project folder.
- Open the terminal (`Ctrl + ~` in VS Code) and run:
  ```sh
  python main.py
  ```
- You have **5 seconds** to switch to Discord before it starts typing.

### **Step 4: Let It Work**
- The script will send each line from `file1.txt` one by one.
- It waits **1.5 seconds** between each command to avoid spamming.

---

## ⚙️ Troubleshooting
### 🔹 Python Not Recognized?
Try using:
```sh
py main.py
```

### 🔹 Script Not Typing?
- Make sure Discord is **active and focused** before running.
- Try running VS Code as **Administrator**.

### 🔹 Commands Are Sent Too Fast?
Increase the delay in `main.py`:
```python
time.sleep(2)  # Change from 1.5 to 2 or more
```

---

## 🚧 Problems Faced
### ❌ Copy-Pasting Many Links Manually
Before automating, I had to manually copy and paste a large number of music commands, which was tedious and time-consuming. This script was created to streamline the process and eliminate repetitive tasks.

---

## 📜 Notes
- This script **does NOT** interact with the Discord API, just simulates key presses.
- If your bot has a cooldown, adjust the `sleep` time accordingly.

Enjoy automating your music commands! 🎶
