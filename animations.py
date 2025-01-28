'''from tkinter import *
import time

WIDTH = 500
HEIGHT = 500

xvel = 2
yvel = 2

window = Tk()


canvas = Canvas(window, width = WIDTH, height = HEIGHT)
canvas.pack()

photo_image = PhotoImage(file = 'momo.gif')
sel_image = canvas.create_image(0, 0 ,image = photo_image, anchor = NW)
image_width = photo_image.width()
image_height = photo_image.height()
ground_image = PhotoImage(file = 'ground.gif')
gr_image = canvas.create_image(0, 0, image = ground_image, anchor = NW)

while True:
    coordinate = canvas.coords(sel_image)
    print(coordinate)
    
    if (coordinate[0] >= (WIDTH-image_width) or coordinate[0] < 0):
        xvel = -xvel
    if (coordinate[1] >= (WIDTH-image_height) or coordinate[1] < 0):
        yvel = -yvel

    canvas.move(sel_image, xvel, yvel)
    
    window.update()
    time.sleep(0.03)

window.mainloop()'''

from tkinter import *

WIDTH = 500
HEIGHT = 500

xvel = 2
yvel = 2

def update_position():
    global xvel, yvel
    coordinate = canvas.coords(sel_image)

    if (coordinate[0] >= (WIDTH-image_width) or coordinate[0] < 0):
        xvel = -xvel
    if (coordinate[1] >= (HEIGHT-image_height) or coordinate[1] < 0):
        yvel = -yvel

    canvas.move(sel_image, xvel, yvel)
    window.after(30, update_position)  # 30 milliseconds delay

window = Tk()

canvas = Canvas(window, width=WIDTH, height=HEIGHT)
canvas.pack()

photo_image = PhotoImage(file='momo.gif')
sel_image = canvas.create_image(0, 0, image=photo_image, anchor=NW)
image_width = photo_image.width()
image_height = photo_image.height()

#ground_image = PhotoImage(file='ground.gif')
#gr_image = canvas.create_image(0, 0, image=ground_image, anchor=NW)

update_position()  # Start the animation

window.mainloop()
