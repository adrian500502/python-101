from tkinter import *

def submit():
    pass

window = Tk()

text = Text(window)
text.pack()

button = Button(window, text="Submit", command=submit)
button.pack()

window.mainloop()