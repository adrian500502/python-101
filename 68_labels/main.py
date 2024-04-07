# label = an area widget that holds text and/or an image within a window

from tkinter import *
window = Tk()

photo = PhotoImage(file='matrix.png')

label = Label(window,
              text="Welcome to the Matrix",
              font=("Arial", 40, "bold"),
              foreground="green",
              background="black",
              relief=RAISED,
              borderwidth=10,
              padx=20,
              pady=20,
              image=photo,
              compound='bottom')
label.pack()
# label.place(x=0, y=0)
# label.place(x=100, y=100)
window.mainloop()