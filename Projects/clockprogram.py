from tkinter import *
from time import *

def update():
    time_string = strftime("%H: %M: %S %p")
    time_label.config(text = time_string)

    day_string = strftime("%A")
    day_label.config(text = day_string)
    print(end = " ")

    date_string = strftime("%B %d, %Y")
    date_label.config(text = date_string)

    window.after(1000,update)

window = Tk()


    


    
time_label = Label(window, font = ("Ariel",40), fg = "green", bg = "black")
time_label.pack()

day_label = Label(window, font = ("Ariel",40), fg = "green", bg = "black")
day_label.pack()


date_label = Label(window, font = ("Ariel",40), fg = "green", bg = "black")
date_label.pack()

update()

window.mainloop()