from words import wordlist
import random
import string


def get_valid_word():

   word = random.choice(wordlist)
   while '-' in word or " " in word:
      word = random.choice(wordlist)

   return word.upper()

def hangman():
   word1 = get_valid_word()
   word_letters = set(word1)
   alphabet = set(string.ascii_uppercase)
   used_letters = set()
   lives = 12


   while len(word_letters) > 0 and lives > 0:
      print(f"You have {lives} lives left")
      print("You have use the letters:",' '.join(used_letters))
      word_list = [letter if letter in used_letters else '-' for letter in word1]
      print("------------------------------")
      print("Current word: ",''.join(word_list))
      print("------------------------------")
      user = input("Type the word:").upper()
      if user in alphabet-used_letters:
         used_letters.add(user)
         if user in word_letters:
            word_letters.remove(user)
         else:
            lives -=1
          

      elif user in used_letters:
         print("You have already used that character.Please try different")

      else:
         print("Invalid character")
      
   if lives == 0:
      print(f"You died!!Sorry!!.The word was {word1}")

   else:
      print(f"You have guessed the word correctly:{word1}")



hangman()

'''
import random
from words import wordlist

import string


def get_valid_word():
    word = random.choice(wordlist)  # randomly chooses something from the list
    while '-' in word or ' ' in word:
        word = random.choice(wordlist)

    return word.upper()


def hangman():
    word1 = get_valid_word()
    word_letters = set(word1)  # letters in the word
    alphabet = set(string.ascii_uppercase)
    used_letters = set()  # what the user has guessed

    lives = 7

    # getting user input
    while len(word_letters) > 0 and lives > 0:
        # letters used
        # ' '.join(['a', 'b', 'cd']) --> 'a b cd'
        print('You have', lives, 'lives left and you have used these letters: ', ' '.join(used_letters))

        # what current word is (ie W - R D)
        word_list = [letter if letter in used_letters else '-' for letter in word1]
        
        print('Current word: ', ' '.join(word_list))

        user_letter = input('Guess a letter: ').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
                print('')

            else:
                lives = lives - 1  # takes away a life if wrong
                print('\nYour letter,', user_letter, 'is not in the word.')

        elif user_letter in used_letters:
            print('\nYou have already used that letter. Guess another letter.')

        else:
            print('\nThat is not a valid letter.')

    # gets here when len(word_letters) == 0 OR when lives == 0
    if lives == 0:
        
        print('You died, sorry. The word was', word1)
    else:
        print('YAY! You guessed the word', word1, '!!')


if __name__ == '__main__':
    hangman()'''
