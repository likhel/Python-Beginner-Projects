'''from tkinter import*

equation_text = ""


def button_n(num):
    global equation_text

    equation_text += str(num)
    equation_label.set(equation_text)

def equal():
    try:
        global equation_text
        total = str(eval(equation_text))
        equation_label.set(total)
        equation_text = total

    except ZeroDivisionError:
        equation_label("Arithmatic error")
        equation_text = ""

    except SyntaxError:
        equation_label.set("Syntax error")
        equation_text = ""

def clear():
    global equation_text
    equation_label.set("")
    equation_text = ""




window = Tk()
window.geometry("500x500")
window.title("CALCULATOR")
equation_label = StringVar()

label = Label(window, textvariable = equation_label, font = ('consolas',20), bg = "white", width = 24, height = 1)
label.pack()

frame = Frame(window, relief= SUNKEN)
frame.pack()

button_1 = Button(frame, text ='1', height = 4, width = 8, font = 35,
                  command = lambda:button_n(1))
button_1.grid(row = 0, column= 0)
button_1.pack()

button_2 = Button(frame, text ='2', height = 4, width = 8, font = 35,
                  command = lambda:button_n(2))
button_1.grid(row = 0, column= 1)
button_1.pack()


button_3 = Button(frame, text ='3', height = 4, width = 8, font = 35,
                  command = lambda:button_n(3))
button_3.grid(row = 0, column=2 )
button_3.pack()


button_4 = Button(frame, text ='4', height = 4, width = 8, font = 35,
                  command = lambda:button_n(4))
button_4.grid(row = 1, column= 0)
button_4.pack()


button_5 = Button(frame, text ='5', height = 4, width = 8, font = 35,
                  command = lambda:button_n(5))
button_5.grid(row = 1, column= 1)
button_5.pack()


button_6 = Button(frame, text ='6', height = 4, width = 8, font = 35,
                  command = lambda:button_n(6))
button_6.grid(row = 1, column= 2)
button_6.pack()


button_7 = Button(frame, text ='7', height = 4, width = 8, font = 35,
                  command = lambda:button_n(7))
button_7.grid(row = 2, column= 0)
button_7.pack()


button_8 = Button(frame, text ='8', height = 4, width = 8, font = 35,
                  command = lambda:button_n(8))
button_8.grid(row = 2, column= 1)
button_8.pack()


button_9 = Button(frame, text ='9', height = 4, width = 8, font = 35,
                  command = lambda:button_n(9))
button_9.grid(row = 2, column= 2)
button_9.pack()

button_0 = Button(frame, text ='0', height = 4, width = 8, font = 35,
                  command = lambda:button_n(0))
button_0.grid(row = 3, column= 0)
button_0.pack()

button_clear = Button(frame, text ='clear', height = 4, width = 12, font = 35,
                  command = clear)
#button_clear.grid(row = 3, column= 1)
button_clear.pack()

plus = Button(frame, text ='+', height = 4, width = 8, font = 35,
                  command = lambda:button_n("+"))
plus.grid(row = 0, column= 3)
plus.pack()

multiply = Button(frame, text ='*', height = 4, width = 8, font = 35,
                  command = lambda:button_n("*"))
multiply.grid(row = 2, column= 3)
multiply.pack()

divide = Button(frame, text ='/', height = 4, width = 8, font = 35,
                  command = lambda:button_n("/"))
divide.grid(row = 3, column= 3)
divide.pack()


minus = Button(frame, text ='-', height = 4, width = 8, font = 35,
                  command = lambda:button_n("-"))
minus.grid(row = 1, column= 3)
minus.pack()

equals = Button(frame, text ='=', height = 4, width = 8, font = 35,
                  command = equal)
minus.grid(row = 3, column= 2)
minus.pack()

button_dec = Button(frame, text ='.', height = 4, width = 8, font = 35,
                  command = lambda:button_n("."))
button_dec.grid(row = 3, column= 1)
button_dec.pack()

window.mainloop()'''

from tkinter import *

equation_text = ""


def button_n(num):
    global equation_text

    equation_text += str(num)
    equation_label.config(text=equation_text)


def equal():
    try:
        global equation_text
        total = str(eval(equation_text))
        equation_label.config(text=total)
        equation_text = total

    except ZeroDivisionError:
        equation_label.config(text="Arithmetic error")
        equation_text = ""

    except SyntaxError:
        equation_label.config(text="Syntax error")
        equation_text = ""


def clear():
    global equation_text
    equation_label.config(text="")
    equation_text = ""


window = Tk()
window.geometry("500x500")
window.title("CALCULATOR")
equation_label = Label(window, text="", font=('consolas', 20), bg="white", width=26, height=1)
equation_label.pack()

frame = Frame(window)
frame.pack()

button_1 = Button(frame, text='1', height=4, width=8, font=35, command=lambda: button_n(1))
button_1.grid(row=0, column=0)

button_2 = Button(frame, text='2', height=4, width=8, font=35, command=lambda: button_n(2))
button_2.grid(row=0, column=1)

button_3 = Button(frame, text='3', height=4, width=8, font=35, command=lambda: button_n(3))
button_3.grid(row=0, column=2)

button_4 = Button(frame, text='4', height=4, width=8, font=35, command=lambda: button_n(4))
button_4.grid(row=1, column=0)

button_5 = Button(frame, text='5', height=4, width=8, font=35, command=lambda: button_n(5))
button_5.grid(row=1, column=1)

button_6 = Button(frame, text='6', height=4, width=8, font=35, command=lambda: button_n(6))
button_6.grid(row=1, column=2)

button_7 = Button(frame, text='7', height=4, width=8, font=35, command=lambda: button_n(7))
button_7.grid(row=2, column=0)

button_8 = Button(frame, text='8', height=4, width=8, font=35, command=lambda: button_n(8))
button_8.grid(row=2, column=1)

button_9 = Button(frame, text='9', height=4, width=8, font=35, command=lambda: button_n(9))
button_9.grid(row=2, column=2)

button_0 = Button(frame, text='0', height=4, width=8, font=35, command=lambda: button_n(0))
button_0.grid(row=3, column=0)

plus = Button(frame, text='+', height=4, width=8, font=35, command=lambda: button_n("+"))
plus.grid(row=0, column=3)

multiply = Button(frame, text='*', height=4, width=8, font=35, command=lambda: button_n("*"))
multiply.grid(row=2, column=3)

divide = Button(frame, text='/', height=4, width=8, font=35, command=lambda: button_n("/"))
divide.grid(row=3, column=3)

minus = Button(frame, text='-', height=4, width=8, font=35, command=lambda: button_n("-"))
minus.grid(row=1, column=3)

equals = Button(frame, text='=', height=4, width=8, font=35, command=equal)
equals.grid(row=3, column=2)

button_dec = Button(frame, text='.', height=4, width=8, font=35, command=lambda: button_n("."))
button_dec.grid(row=3, column=1)

Clear = Button(window, text='clear', height=2, width=12, font=25, command=clear)
Clear.pack()



window.mainloop()







