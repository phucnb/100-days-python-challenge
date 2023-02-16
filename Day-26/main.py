import pandas as pd

#TODO 1. Create a dictionary in this format:
data = pd.read_csv('nato_phonetic_alphabet.csv')

data_dict = {row.letter : row.code for (index, row) in data.iterrows()}


#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
name = input("What's is your name?: ").strip()
name_list = [word.upper() for word in name]
result = [data_dict[letter] for letter in name_list]

print(result)




