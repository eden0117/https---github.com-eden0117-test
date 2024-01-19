import time 
import tkinter as tk
from tkinter import simpledialog
import pyautogui
USER_INP = ""
def on_key_press(USER_INP):
    print(USER_INP)
    pyautogui.typewrite(USER_INP,interval=0.005)
    exit()
if __name__ == "__main__":
    
    ROOT = tk.Tk()
    ROOT.withdraw()
    USER_INP = simpledialog.askstring(title="Copy & Paste in 5 Sec",prompt="Please input\t\t\t\t\t\t")
    if  USER_INP :
        time.sleep(5)
        on_key_press(USER_INP)
    else:
        exit()

    
    