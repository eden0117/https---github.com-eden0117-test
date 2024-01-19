import time,sys 
import pyperclip
import keyboard
USER_INP = ""

if __name__ == "__main__":
    t = time.time() 
    while time.time() - t <= 5*60:
        if keyboard.is_pressed("ctrl"):
            if keyboard.is_pressed("c"):
                USER_INP = pyperclip.paste()
                continue
            if keyboard.is_pressed("v"):
                keyboard.write(USER_INP,0.003)#0.005
                break
    sys.exit(0)
    
    