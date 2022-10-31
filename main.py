import sys
import string

def encrypt(key,char):
    chars = string.ascii_uppercase
    return chars[(chars.find(char)*key[0] + key[1]) % 26]

if __name__ == "__main__":
    plain = input(" [+] enter plaintext: ").upper()
    key = input(" [+] enter key: ").split(",")
    ciphertext = ""

    for char in plain:
        ciphertext += encrypt(key,char)
    
    print(ciphertext)
