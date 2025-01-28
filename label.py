from tkinter import *

window = Tk()
photo = PhotoImage(file = 'football.gif')
label = Label(window,
                text = "NoIcE", 
                font = ("Callibri",40,"bold"),
                fg = "Green",
                bg= "Black",
                relief = RAISED,
                bd = 20,
                padx = 20,
                pady = 20,
                image = photo,
                compound = 'top')
#label.place(x=50,y=50)
label.pack()
window.mainloop()