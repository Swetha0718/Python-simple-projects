name="""
 _     ____  _      _____ _      ____  _        _____ ____  _      _____
/ \ /|/  _ \/ \  /|/  __// \__/|/  _ \/ \  /|  /  __//  _ \/ \__/|/  __/
| |_||| / \|| |\ ||| |  _| |\/||| / \|| |\ ||  | |  _| / \|| |\/|||  \  
| | ||| |-||| | \||| |_//| |  ||| |-||| | \||  | |_//| |-||| |  |||  /_ 
\_/ \|\_/ \|\_/  \|\____\\_/  \|\_/ \|\_/  \|  \____\\_/ \|\_/  \|\____\
                                                                        
"""
print(name)
words=["chennai","coimbatore","trichy","salem","tripur","bangalore"]
import random
import hangman_stages
lives=6
choosen_word=random.choice(words)
print(choosen_word)
display=[]
for i in range(len(choosen_word)):
    display+="_"
print(display)
game_over=False
while not game_over:
    guessed_letter=input("Guess any letter: ").lower()
    for position in range(len(choosen_word)):
        letter=choosen_word[position]
        if letter==guessed_letter:
            display[position]=guessed_letter
    print(display)
    if guessed_letter not in choosen_word:
        lives-=1
        if lives==0:
            game_over=True
            print("You lose!!")
    if '_' not in display:
        game_over=True
        print("You win!!")
    print(hangman_stages.stages[lives])