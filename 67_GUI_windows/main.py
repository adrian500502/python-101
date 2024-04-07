from tkinter import *

# widgets = GUI elements: buttons, textboxes, labels, images
# windows = server as a container to hold or contain these widgets

window = Tk() # instantiate an instance of a window
window.geometry("500x500")
window.title("First GUI program")

icon = PhotoImage(file="logo.png")
window.iconphoto(True, icon)
# window.config(background="black")
window.config(background="#5cfcff")

window.mainloop() # place window on computer screen, listen for events