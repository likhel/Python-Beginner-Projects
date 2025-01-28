import random

def play():
    
    person = None
    choices = ['r','s','p']
    
    computer = random.choice(choices)
    while person not in choices:
      person = input("Enter 's' for scissors,'r' for rock or 'p' for paper: ").lower() 
    print(f"computer:{computer}")
    print(f"You:{person}")
    if person == computer:
        return "Tie"
    if win(person, computer) is True:
        return "You won..."
    return "You lost"
       
    


def win(player1, opponent):
    
    if (player1 == 'r' and opponent == 's') or (player1 == 's' and opponent == 'p') or (player1 == 'p' and opponent == 'r'):
      return True

def new_game():
      
    ans = input("Do you want to play again(Y/N)?:").lower()
    return ans
     
          

      

while True:
    
        result = play()
        print(result)
        again = new_game()
        while again != 'y'  and again != 'n':
            again = new_game()
        if again == 'n':
            break
     

        
            
      
        
      
   
        
        


   
    
       



