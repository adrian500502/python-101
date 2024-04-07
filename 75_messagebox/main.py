from tkinter import *
from tkinter import messagebox  # import messagebox library


def click():
    # messagebox.showinfo(title="This is an info message box", message="You are a person")
    # messagebox.showwarning(title="Warning", message="You have been warned")
    # messagebox.showerror(title="Error", message="Something went wrong")

    # if messagebox.askokcancel(title="Ask ok cancel", message="Do you want to continue?"):
    #     print('You continue smtn')
    # else: print('You canceled smtn')

    # if messagebox.askretrycancel(title="Ask retry cancel", message="Do you want to retry?"):
    #     print('You retried smtn')
    # else:
    #     print('You canceled smtn')

    # if messagebox.askyesno(title="Ask yes or now", message="Do you like pizza?"):
    #     print("I like pizza too!")
    # else: print("Why do you not like pizza? :o")

    # answer = messagebox.askquestion(title="Ask question", message="Do you like apples?")
    # if answer == 'yes': print("I like apples too!")
    # else: print("Why do you not like apples? :o")

    answer = messagebox.askyesnocancel(title="Yes no cancel", message="Do you like to code?", icon="question")
    if answer:
        print("You like to code")
    elif not answer:
        print("You don't like to code")
    else:
        print("You have dodged the question")

window = Tk()

button = Button(window, command=click, text='Click me')
button.pack()

window.mainloop()
