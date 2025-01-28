import random
while True:

 choices = ["rock","paper","scissors"]
 computer = random.choice(choices) 
 person = None

 while person not in choices:
    person = input("Enter your choice(rock,paper,scissors):").lower()

 print("Computer:",computer)
 print("Player:",person)

 if computer == person:
        print("Game Tie...")

 elif computer == "paper":
    if person == "scissors":
        print("You won!")
    elif person == "rock":
        print("You loss!")
 elif computer == "rock":
    if person == "scissors":
        print("You won!")
    elif person == "paper":
          print("You loss!")

 elif computer == "scissors":
    if person == "rock":
           print("You won!")
    elif person == "paper":
           print("You loss!")
   
 play_again = input("Do you want to play again:(yes/no)").lower()
     
 if play_again != "yes":
        break
    
