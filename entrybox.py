#entry widget : box which accepts only one line of sentence

from tkinter import *

def submit():
    pd = entry.get()
    print(f"passoword : {pd} ")
    entry.config(state = DISABLED)
    

def delete():
    entry.delete(0,END)

def backspace():
    entry.delete(len(entry.get())-1,END)


window = Tk()


entry = Entry(window,
              font = ("Arial",25),
              fg = "#00FF00",
              bg = "black",
              show = "*")
#entry.insert(0,"password:")
#entry.config(show = "*")
entry.pack(side = LEFT)

submit_button = Button(window,text = "Submit",command = submit)
submit_button.pack(side = RIGHT)

delete_button = Button(window,text = "delete",command = delete)
delete_button.pack(side = RIGHT)

backspace_button = Button(window,text = "backspace",command = backspace)
backspace_button.pack(side = RIGHT)

window.mainloop()