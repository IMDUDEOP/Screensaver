import tkinter as tk
import time
import psutil
from datetime import datetime
import sys

def update():
    now = datetime.now()
    time_str = now.strftime("%H:%M:%S")
    date_str = now.strftime("%A, %d %B %Y")

    battery = psutil.sensors_battery()
    if battery:
        battery_str = f"{battery.percent:.0f}% {'🔌' if battery.power_plugged else '🔋'}"
    else:
        battery_str = "Battery N/A"

    time_label.config(text=time_str)
    date_label.config(text=date_str)
    battery_label.config(text=battery_str)
    
    root.after(1000, update)

def close(event=None):
    root.destroy()
    sys.exit()

root = tk.Tk()
root.attributes('-fullscreen', True)
root.configure(bg='#121212')
root.config(cursor="none")

#exit on any input
root.bind("<Any-KeyPress>", close)
root.bind("<Button>", close)
root.bind("<Motion>", close)

font_main = ("Helvetica Neue", 80, "bold")
font_sub = ("Helvetica Neue", 28, "normal")

time_label = tk.Label(root, font=font_main, fg="#FFFFFF", bg="#121212")
time_label.pack(pady=20)

date_label = tk.Label(root, font=font_sub, fg="#AAAAAA", bg="#121212")
date_label.pack(pady=10)

battery_label = tk.Label(root, font=font_sub, fg="#00FFAA", bg="#121212")
battery_label.pack(pady=5)

update()
root.mainloop()
