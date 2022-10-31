from Alphabet import alphabet # Import small letters
from Art import logo # Import logo
import pyfiglet

def caesar(text, shift_amount, choice):
    modified_text = ""
    for letter in text:
        if letter in alphabet:
            index = alphabet.index(letter) # Get index in alphabet list of text letters
            if(choice == 'encode'):
                shift_index = index + shift_amount # Get index after shifting
                if(shift_index >= len(alphabet)): #If its out of bound
                    shift_index -= len(alphabet) # Decrease it by length of alphabet
            elif(choice == 'decode'):
                shift_index = index - shift_amount # Get index after shifting
            modified_text += alphabet[shift_index] # Collect the letters after shifting
        else:
            modified_text += letter
    print(f"Your message after {choice}d --> {modified_text}")


print(logo)

keep_continue = True
while(keep_continue):
    choice = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(text, shift, choice)

    want_continue = input("Continue? 'yes' to continue. 'no' to stop.")
    if(want_continue == 'no'):
        keep_continue = False
        Bye = pyfiglet.figlet_format("Good Bye!") # ASCII ART
        print(Bye)
