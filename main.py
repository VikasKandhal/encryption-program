#Encryption Program
#using python
import random
import string

chars =" " + string.punctuation + string.digits + string.ascii_letters
chars = list(chars)
key = chars.copy()

random.shuffle(key)

#print(f"Chars : {chars}")
#print(f"Key : {key}")


#ENCRYPT

plain_text = input("Enter a message to encrypt:")
cipher_text = ""

for letter in plain_text:
  index = chars.index(letter)
  cipher_text += key[index]

print(f"Original Message:{plain_text}")
print(f"Encrypted Message:{cipher_text}")

#DECRYPT

cipher_text_text = input("Enter a message to decrypt:")
plane_text = ""

for letter in cipher_text:
  index = key.index(letter)
  plane_text += chars[index]

print(f"Encrypted Message:{cipher_text}")
print(f"OriginalMessage:{plain_text}")

//ends

