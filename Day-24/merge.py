#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
with open("Day-24/Input/Letters/starting_letter.txt", 'r') as file:
    template = file.readlines()
with open("Day-24/Input/Names/invited_names.txt", 'r') as file:
    names = [name.strip('\n') for name in file.readlines()]

letter = template[:]
for name in names:
    letter[0] = template[0].replace("[name]", name)
    with open(f"Day-24/Output/ReadyToSend/letter_for_{name}.txt", 'w') as file:
        file.write(''.join(letter))


