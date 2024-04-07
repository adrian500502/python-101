from tkinter import *

def submit():
    print("The temperature is:", scale.get(), "degrees Celsius")

window = Tk()

hot_image = PhotoImage(file="fire.png")
hot_label = Label(image=hot_image)
hot_label.pack()

scale = Scale(window,
              from_=100,
              to_=0,
              length=600,
              orient=VERTICAL, # orientation of scale
              font=('Consolas', 20),
              tickinterval=10, # adds numeric indicators for value
              showvalue=0, # hides current value
              resolution=5, # increment of slider
              troughcolor="#69EAFF",
              fg="#FF1C00",
              bg="black"
              )
scale.set(((scale['from']-scale['to']) / 2) + scale['to']) # set current value of slider
scale.pack()

cold_image = PhotoImage(file="snowflake.png")
cold_label = Label(image=cold_image)
cold_label.pack()

button = Button(window,
                text="Submit",
                command=submit)
button.pack()

window.mainloop()