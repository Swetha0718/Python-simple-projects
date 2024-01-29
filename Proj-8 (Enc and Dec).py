alphabets=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
def encryption(plain_text,shift_key):
    cipher_text=[]
    for char in plain_text:
        if char in alphabets:
            position=alphabets.index(char)
            new_position=(position+shift_key)%26
            cipher_text+=alphabets[new_position]
        else:
            cipher_text+=char

    print(f"Here is the encryption of the plain text: {cipher_text}")

def decryption(cipher_text,shift_key):
    plain_text=[]
    for char in cipher_text:
        if char in alphabets:
            position=alphabets.index(char)
            new_position=(position-shift_key)%26
            plain_text+=alphabets[new_position]
        else:
            plain_text+=char

    print(f"Here is the decryption of the cipher text: {plain_text}")

wanna_end=False
while not wanna_end:
    what_to_do=input("Type enc for encrypt or dec for decrypt: ")
    text=input("Enter any msg: ")
    key=int(input("Enter the key value: "))
    if what_to_do=="enc":
        encryption(plain_text=text,shift_key=key)
    elif what_to_do=="dec":
        decryption(text,key)
    play_again=input("Type 'yes' to continue or 'no' to exit: ")
    if play_again=="no":
        wanna_end=True
        print("Game over")
