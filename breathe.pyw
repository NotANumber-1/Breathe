import tkinter as tk
from tkinter.constants import HORIZONTAL
import tkinter.ttk as ttk
import time
root = tk.Tk()
root.iconbitmap("app.ico")
root.title("Breathe by codingPro01")
root.geometry("512x128")
destxt = tk.Label(text="Ready: Press [s] to start", font=("Arial", 16))
destxt.pack()
destxt.place(x=16, y=16)

pgbar = ttk.Progressbar(root, orient=HORIZONTAL, length=384, mode="determinate")
pgbar.pack()
pgbar.place(x=64, y=64)

def start(_=any):
    brin()
    brhd()
    brot()
    cldn()
    destxt.configure(text="Ready: Press [s] to start")

def brin():
    destxt.configure(text="Breathe in")
    root.update()
    for i in range(100):
        root.update()
        pgbar["value"] += 1
        time.sleep(0.04)

def brhd():
    destxt.configure(text="Hold breath")
    for i in range(100):
        time.sleep(0.04)
        root.update()

def brot():
    destxt.configure(text="Breathe out")
    root.update()
    for i in range(100):
        root.update()
        pgbar["value"] -= 1
        time.sleep(0.04)

def cldn():
    destxt.configure(text="Cooldown")
    root.update()
    for i in range(100):
        root.update()
        pgbar["value"] += 1
        time.sleep(0.005)
    for i in range(100):
        root.update()
        pgbar["value"] -= 1
        time.sleep(0.005)

root.bind("<s>", start)

root.mainloop()