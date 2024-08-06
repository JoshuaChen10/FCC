text = 'hello there general kenobi'
custom_key = 'Shmungus'

# Initial inputted text and encryption key for the cipher.

# Initialize function for the soon to follow cipher.
def cipher(text, custom_key, direction=1):
    start_Index = 0
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    ciphered_Text = ''
    # Initializes the beginning index for our string, the alphabet we are attributing to the text, and the ciphered text.
    # values to, and the string where we intend to append our ciphered text.

    for char in text.lower():
        # loops through each of the characters in our initial text string.
        if not char.isalpha():
            ciphered_Text += char
        
        else:
            cipher_Char = custom_key[start_Index % len(custom_key)]
            # The cipher character index i determined by the remainder of our starting
            # index and our custom key length.
            start_Index +=1
            # Increments the starting index by 1.

            index = alphabet.find(char)
            # Finds the index of the character in the alphabet according to current index.
            offset = alphabet.index(cipher_Char.lower())
            # Finds the index of the cipher character in the alphabet.
            new_Index = (index + offset * direction) % len(alphabet)
            # finds the new index of our characetr within the alphabet using the offset..
            ciphered_Text += alphabet[new_Index]
            # Appends new character to our encrypted text with each loop.
    return ciphered_Text

def encrypt(text, custom_key):
    return cipher(text, custom_key)
#This function returns our encrypted string

def decrypt(text, custom_key):
    return cipher(text, custom_key, -1)
# This function returns our decrypted string

print(f'\ntext: {text}\n')
# Prints our initial text.
print(f'key: {custom_key}\n')
#Prints our custom key.
decryption = decrypt(text, custom_key)
encryption = encrypt(text, custom_key)
# These set encryption and decryption variables
print(f'encrypted text: {encryption}\n')
# Prints out the encrypted form of our text.




