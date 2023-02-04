import platform    # Used to clear screen
import subprocess  # Used by clear screen
from art import * #https://pypi.org/project/art/
import word_list
import random
import os
import time
import sys

def clear_screen():
    '''
    To clear screen
    by ePi272314
    https://stackoverflow.com/questions/60783120/ascii-animation-on-python
    '''
    command = "cls" if platform.system().lower()=="windows" else "clear"
    subprocess.call(command) == 0
        
def text_art_animations():
    '''
    Play text art animations in the terminal
    https://github.com/rvizzz/text_art_animations
    '''

    folder_name = 'rick_ascii'
    loops = 2

    if not os.path.isdir(folder_name):
        print(folder_name + " could not be found")
        sys.exit(0)

    files_exist = True
    num_found = 0

    text_files = []

    while files_exist:
        file_name = folder_name + "/" + str(num_found) + ".txt"
        
        if os.path.isfile(file_name):
            f = open(file_name, "r")
            text_files.append(f.read())
            num_found += 1
        else:
            files_exist = False

    if len(text_files) == 0:
        print(folder_name + " did not have text art files")
        sys.exit(0)

    i = 0
    first = True
    backspace_adjust = (len(text_files[0].split("\n")) + 1) * "\033[A"

    while i < loops or loops == -1:
        for text_file in text_files:

            if not first:
                print(backspace_adjust)
            
            print(text_file)
            
            first = False
            time.sleep(.05)
            
        i += 1
        
def main():
    
    # Initial variable
    welcome=text2art("Hangman",font='rnd-xlarge',chr_ignore=True)
    lives_level = ['loading1','loading2','loading3','loading4','loading5','loading6']    
    lives = 6
    guess_word = ''

    clear_screen()
    print(welcome)

    # Pick a random word from list
    word = random.choice(word_list.word_list)

    # create new string with all underscore '_' with same length of word
    for _ in range(len(word)):
        guess_word += "_"
        
    # Print ______
    tprint(guess_word,font="block",chr_ignore=True)

    # Loop until answer wrong 6 times
    while lives > 0:
        
        # Check if guess all the letters
        if guess_word == word:
            clear_screen()
            # print art animation
            text_art_animations()
            break
            
        # Print Lives bar remain using art library
        # lives_level is a dict with 6 different loading arts from 1->6 from art library
        print(f"Lives remain: {art(lives_level[lives - 1])}")
        
        # Keep asking until user enter ONLY 1 letter
        while True:
            guess_letter = input("Guess a letter: ").lower()
            if len(guess_letter) == 1:
                break
        count = 0
        # If the letter is already guessed before, then also minus lives
        if guess_letter in guess_word:
            lives -= 1
        # if the word has the letter
        elif guess_letter in word:
            
            # find index of the letter
            index = word.find(guess_letter)
            # loop in case there are multiple letters in the word
            while index != -1:
                count += 1
                # Update guess_word with the letter
                guess_word = guess_word[:index] + guess_letter + guess_word[index + 1:]
                # then find index of the next letter
                index = word.find(guess_letter, index + 1)
        
        # if the letter doesn't appear in the word
        else:
            lives -= 1

        clear_screen()
        # print the updated guess_word with the letter
        tprint(guess_word,font="block",chr_ignore=True)
        if count > 1:
            print(f"There are {count} letters '{guess_letter.upper()}' in the word")
        else:
            print(f"There is {count} letter '{guess_letter.upper()}' in the word")
    
    
    clear_screen()
    # print LOSE if wrong 6 times
    if lives == 0:
        tprint('LOSE',font="random-xlarge",chr_ignore=True)
        
if __name__ == "__main__":
    main()