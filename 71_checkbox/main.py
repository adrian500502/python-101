from tkinter import *

def display():
    # if x.get() == 1:
    if x.get():
        print("You agree!")
    else: print("You did not agree!")

window = Tk()

# x = IntVar()
x = BooleanVar()

python_photo = PhotoImage(file="python.png")

check_button = Checkbutton(window,
                           text="I agree to something",
                           variable=x,
                           # onvalue=1,
                           onvalue=True,
                           # offvalue=0,
                           offvalue=False,
                           command=display,
                           font=("Arial", 20),
                           fg="#00FF00",
                           bg="black",
                           activeforeground="#00FF00",
                           activebackground="black",
                           padx=25,
                           pady=10,
                           image=python_photo,
                           compound=LEFT)
check_button.pack()

window.mainloop()