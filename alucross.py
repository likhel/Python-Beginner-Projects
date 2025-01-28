from tkinter import *
import random


def next_turn(row,column):
    global player 
    if but[row][column]["text"] == "" and check_winner() is False:
        if player == players[0]:
            but[row][column]["text"] = player
            if check_winner() is False:
                player = players[1]
                label.config(text = (player + " turn"))

            elif check_winner() is True:
                label.config(text = (player + " wins"))
            
            elif check_winner() == "Tie":
                label.config(text = ("It is a Tie"))

        else:
         
            but[row][column]["text"] = player
            if check_winner() is False:
                player = players[0]
                label.config(text = (player + " turn"))

            elif check_winner() is True:
                label.config(text = (player + " wins"))
            
            elif check_winner() == "Tie":
                label.config(text = ("Tie"))



def check_winner():
    for row in range(3):
        if but[row][0]['text'] == but[row][1]['text'] == but[row][2]['text'] != "":
            but[row][0].config(bg = "green")
            but[row][1].config(bg = "green")
            but[row][2].config(bg = "green")
            return True
    
    for column in range(3):
        if but[0][column]['text'] == but[1][column]['text'] == but[2][column]['text'] != "":
            but[0][column].config(bg = "green")
            but[1][column].config(bg = "green")
            but[2][column].config(bg = "green")
            return True
        
    if but[0][0]['text'] == but[1][1]['text'] == but[2][2]['text'] != "":
            but[0][0].config(bg = "green")
            but[1][1].config(bg = "green")
            but[2][2].config(bg = "green")
            return True
    elif but[0][2]['text'] == but[1][1]['text'] == but[2][0]['text'] != "":
            but[0][2].config(bg = "green")
            but[1][1].config(bg = "green")
            but[2][0].config(bg = "green")
            return True
    elif empty_spaces() is False:
            for row in range(3):
                 for column in range(3):
                      but[row][column].config(bg = "red")
            return "Tie"
    else:
         return False    

        
    


def new_game():
     global player 
     player = random.choice(players)
     label.config(text = (player + " turn"))

     for row in range(3):
          for column in range(3):
               but[row][column].config(text = "", bg = "white")


def empty_spaces():
     
     spaces = 9
     for row in range(3):
          for column in range(3):
               if  but[row][column]['text'] != "":
                    spaces -= 1
    
     if spaces == 0:
          return False

     else:
          return True
     

window = Tk() 
window.title("AluCross")

players = ['x','o']
player = random.choice(players)

label = Label(text = player + " turn", font = ("Calibri",30))
label.pack(side = 'top')
restart_game = Button(text = 'restart',font = ("Calibri",20), command = new_game)
restart_game.pack(side = 'top')
frame = Frame(window)
frame.pack()

but = [[0,0,0],
      [0,0,0],
      [0,0,0]]

for row in range(3):
    for column in range(3):
        but[row][column] = Button(frame, text = "", font = ("Calibri",40), width = 5, height = 2,
                                  command = lambda row = row, column = column: next_turn(row,column))
        but[row][column].grid(row = row, column = column )





window.mainloop()