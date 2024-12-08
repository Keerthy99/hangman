import random
import hangman_words
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

logo = ''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    '''

                                                                    
                                                                    


choosen_word=random.choice(hangman_words.word_list)
# print(choosen_word)

display=[]
word_length=len(choosen_word)
lives=6

for i in range(word_length):
    display+="_"
    

end_of_game=False
while not end_of_game:
    guess_letter=input('guess a letter: ').lower()
    if guess_letter in display:
        print(f"You have already gussed{guess_letter}")
    for position in range(word_length):
        letter=choosen_word[position]
        if letter==guess_letter:
            display[position]=letter
    if guess_letter not in choosen_word:
        lives-=1
        if lives==0:
            end_of_game=True
            print("You loose")


    # print(display)

    if "_" not in display:
        end_of_game=True
        print("You win")
    print(stages[lives])
print(f"The word is {choosen_word}")   
   