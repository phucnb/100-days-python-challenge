from art import *
import ascii


def main():
    print(text2art("Vigenère Cipher",font='rnd-xlarge',chr_ignore=True))
    while True:
        print("1. Encrypt")
        print("2. Decrypt")
        print("3. Exit")
        
        while True:
            selection = input("Selection: ")
            if selection in ['1', '2', '3']:
                break
        
        if selection == '1':
            text = input("Enter plain text: ")
            while True:
                key = input("Enter key: ")
                if len(key) > 0:
                    break
            print(f"Ciphertext is: {encrypt(text, key)}")
            print("\n\n")
            
        elif selection == '2':
            cipher = input("Enter ciphertext: ")
            while True:
                key = input("Enter key: ")
                if len(key) > 0:
                    break
            print(f"Text is: {decrypt(cipher, key)}")
            print("\n\n")        
        else:
            exit()
    
    
def encrypt(text, key):
    '''
        The function have 2 parameters text and key
        the function will return encrypted of text
    '''
    cipher = ''
    # Check if key is shorter than text, if then repeat the key
    key = generate_key(text, key) if len(key) < len(text) else key
    for letter in range(len(text)):
        index = (ascii.list.index(text[letter]) + ascii.list.index(key[letter])) % 95
        cipher += ascii.list[index]
        
    return cipher
    
def decrypt(cipher, key):
    '''
        The functions has 2 parameters cipher and key
        and will return decrypted of cipher
    '''
    text = ''
    key = generate_key(cipher, key) if len(key) < len(cipher) else key
    for letter in range(len(cipher)):
        index = (ascii.list.index(cipher[letter]) - ascii.list.index(key[letter]))
        if index < 0:
            index += 95
        text += ascii.list[index]
    return text
    
def generate_key(text, key):
    '''
        The function will return the key which have the same length as text
        If the key is longer than text then just return the key 
        even the function won't be called if key longer than text
    '''    
    while len(key) < len(text):        
        for index in range(len(key)):
            key += key[index]
            if len(key) == len(text):
                break
    return key
    
    
if __name__ == "__main__":
    main()