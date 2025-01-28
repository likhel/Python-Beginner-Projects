#widgets :gui elements(icons,buttons,textboxes,lables)
#windows : serves as a  container to hold these widgets


from tkinter import *

windows = Tk() #instantiates an instance of a window 
windows.geometry("620x620") 
windows.title("my first gui windows program")
icon = PhotoImage(file = 'football.gif')#changes photo types to photo image which is understood by python
windows.iconphoto(True,icon)
windows.config(background = "#8e5cf2")

windows.mainloop() #place window on computer screen
