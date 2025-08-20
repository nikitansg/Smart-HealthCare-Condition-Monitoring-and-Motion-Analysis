import os
import body_data
import human
import tkinter as tk
from PIL import Image, ImageTk
window = tk.Tk()
window.title("Health monitoring System")
path = 'logo.jpg'
img = ImageTk.PhotoImage(Image.open(path))
panel = tk.Label(window, image = img)
panel.pack(side = "bottom", fill = "both", expand = "yes")
def body():
    human.run()

def activity():
    body_data.run_body()

takeImg = tk.Button(window, text="BODY POSE", command=body  ,fg="white"  ,bg="grey"  ,width=10  ,height=1, activebackground = "aqua" ,font=('times', 15, ' bold '))
takeImg.place(x=100, y=280)

trainImg = tk.Button(window, text="POSE CORRECTION", command=activity  ,fg="white"  ,bg="blue"  ,width=15  ,height=1, activebackground = "gold" ,font=('times', 15, ' bold '))
trainImg.place(x=260, y=280)
window.mainloop()
