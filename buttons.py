from tkinter import *
count = 0
def click():
    global count
    count +=1
    print(count)


window = Tk()
photo = PhotoImage(file = "football.gif")
button = Button(window,
                   text = "click here",
                   command =click ,
                   font = ("Ariel",25),
                   fg = '#34eb3d',
                   bg = "black",
                   activeforeground = "#34eb3d",
                   activebackground = "black",
                   state = ACTIVE,
                   image = photo,
                   compound = "bottom")
button.pack()
window.mainloop()


