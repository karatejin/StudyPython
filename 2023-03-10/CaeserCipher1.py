## 카이사르 암호

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")

text = input("Type your message:\n").lower()

shift = int(input("Type the shift number:\n"))

#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.

def encrypt(text, shift):

    #TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.  


    ##🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛
    if direction == "encode":
        cipher_text = ""

        for letter in text:
            position = alphabet.index(letter)
            new_position = position + shift
            new_letter = alphabet[new_position]
            cipher_text += new_letter
        print(f"The encoded text is: {cipher_text}")
        return cipher_text

#TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message. 
print(encrypt(text, shift))