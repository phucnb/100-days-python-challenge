#Password Generator Project
import random
import re
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
while True:
    nr_symbols = int(input(f"How many symbols would you like?\n"))
    if nr_symbols > nr_letters:
        pass
    else:
        break
while True:
    nr_numbers = int(input(f"How many numbers would you like?\n"))
    if nr_numbers > (nr_letters - nr_symbols):
        pass
    else:
        break


password = []

for letter in range(1, nr_letters + 1):
    if letter in range(1, nr_symbols + 1):
        password.append(random.choice(symbols))
    elif letter in range(nr_symbols + 1, nr_symbols + nr_numbers + 1):
        password.append(random.choice(numbers))
    else:
        password.append(random.choice(letters))
      
random.shuffle(password)  

print(''.join(password))