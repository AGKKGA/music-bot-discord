import pyautogui
import time

# Delay to switch to Discord before script starts (adjust if needed)
time.sleep(5)

# Open and read file1.txt
with open("file1.txt", "r", encoding="utf-8") as file:
    for line in file:
        line = line.strip()  # Remove extra spaces or newlines
        if line:  # Avoid sending empty lines
            pyautogui.write(line)  # Type the command
            pyautogui.press("enter")  # Press Enter to send
            time.sleep(5)  # Wait before sending the next one
