import tkinter as tk
import ctypes
import os 
import pandas as pd
from pathlib import Path
from tkinter import filedialog as fd
root = tk.Tk()
root.wm_withdraw()
file_path = fd.askopenfilenames(parent=root,title="Choose Excel Files to Convert")
response = ""
for p in file_path:
    if p[-4:] == "xlsx":
        curr = p[:-4]+"csv"
    elif p[-3:] == "xls":
        curr = p[:-3]+"csv"
    else:
        response += "『"+ os.path.basename(p) + "』 is not a xlsx or xls file \n"
        continue
    if Path(curr).is_file():
        response += "『"+os.path.basename(curr) + "』 exist please delete it first !! \n"
        continue
    df = pd.read_excel(p)
    df.to_csv(curr,encoding="utf_8_sig",header=False)
    response += "『"+ os.path.basename(curr) + "』successfully created \n"

def Mbox(title,text,style):
    return ctypes.windll.user32.MessageBoxW(0, text, title, style)

if response == "":
    Mbox("Result","No File Converted",1)
else:
    Mbox("Result",response,1)