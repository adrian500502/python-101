from tkinter import *
from tkinter import colorchooser # submodule

def click():
    # color = colorchooser.askcolor()
    # color_hex = color[1]
    # window.config(bg=color_hex)
    window.config(bg=colorchooser.askcolor()[1])

window = Tk()
window.geometry("500x500")

button = Button(text="Click me", command=click)
button.pack()

window.mainloop()

