import string


lowercase_alphabets = list(string.ascii_lowercase)
objective=input('Type "encrypt" to encrypt or "decrypt" to decrypt\n').lower()
text=input("Enter your text:\n").lower()
shifter=int(input("Enter shift number:\n"))

def encrypt(original_text,shift_amount):
    ciphertext=""
    for letter in original_text:
        shifted_position=lowercase_alphabets.index(letter)+shift_amount
        shifted_position%=len(lowercase_alphabets)
        ciphertext+=lowercase_alphabets[shifted_position]
    print(f"Here is the encrypted text: {ciphertext}")



def decrypt(original_text,shift_amount):
    decryptedtext=""
    for letter in original_text:
        shifted_position=lowercase_alphabets.index(letter)-shift_amount
        shifted_position%=len(lowercase_alphabets)
        decryptedtext+=lowercase_alphabets[shifted_position]
    print(f"Here is the decrypted text: {decryptedtext}")
    
if objective=="encrypt":
    encrypt(original_text=text,shift_amount=shifter)
elif objective=="decrypt":
    decrypt(original_text=text, shift_amount=shifter)
else:
    print("Invalid input!")
