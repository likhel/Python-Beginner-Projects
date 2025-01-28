#radiobuttons: same as check box,but only one can be selected from the group
from tkinter import *

food = ["chowmein","momo","chicken_drumstick"]

window = Tk()

def order():
    if x.get() == 0:
     print("you ordered chowmein")
   
    elif x.get() == 1:
     print("you ordered momo")
     
    else:
     print("you ordered chicken drumstick")


chowmeinimage = PhotoImage(file = "chowmein.gif")
momoimage = PhotoImage(file = "momo.gif")
drumstickimage = PhotoImage(file = "drumstick.gif")

cc = [chowmeinimage, momoimage, drumstickimage ]

x = IntVar()

for i in range(len(food)):
 
  radio_buttons = Radiobutton(window,
                              text =food[i], # adds texts to radiobuttons
                              font = ("Impact",25),
                              variable = x,# groups radiobutton if they share a same variable
                              value = i, # assigns  different values to each radiobutton
                              padx = 20,
                              
                              image = cc[i],
                              compound = "left", # adds image to the left side of text
                              indicatoron = 0, # eliminate circle indicators
                              width = 350,
                              command = order,
                            )
 
  radio_buttons.pack(anchor = W)

window.mainloop()