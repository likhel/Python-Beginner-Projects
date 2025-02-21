import random


CHOICES = {'r': 'rock', 's': 'scissors', 'p': 'paper'}

def play():
    person = None
    computer_key = random.choice(list(CHOICES.keys()))
    
    while person not in CHOICES:
        person = input("Enter 'r' for rock, 's' for scissors, or 'p' for paper: ").lower()
    
    print(f"Computer: {CHOICES[computer_key]}")
    print(f"You: {CHOICES[person]}")
    
    if person == computer_key:
        return "Tie"
    if win(person, computer_key):
        return "You won!"
    return "You lost."

def win(player1, opponent):
    rules = {'r': 's', 's': 'p', 'p': 'r'}  # Rock beats scissors, scissors beat paper, paper beats rock
    return rules[player1] == opponent

def new_game():
    while True:
        ans = input("Do you want to play again (Y/N)?: ").lower()
        if ans in ['y', 'n']:
            return ans
        print("Invalid input. Please enter 'Y' or 'N'.")


while True:
    result = play()
    print(result)
    again = new_game()
    if again == 'n':
        break