#Code taken from this.py
#Original code available at %LocalAppData%/Programs/Python/Pythonver/lib/this.py

#ROT13 Encryption and decryption programs-use this to hide text to bypass text filters

print("This is a ROT13 encoder. You can use this to encrypt words so that you can send secret messages.")
print("However, numbers, punctuation and special characters will not have their positions changed.")
print("This means if your secret message gets leaked to any third party, they will still get the numbers enclosed in your text.")
s=input("Enter the text to encrypt/decrypt> ")

#Code to encode the text in rot13
e="Created by Aaryaman Chitnavis-Class 8B 2023-24, Arya Vidya Mandir, Juhu on August 1, 2023."
d={}
for c in (65, 97):
    for i in range(26):
        d[chr(i+c)] = chr((i+13) % 26 + c)

print("".join([d.get(c, c) for c in s]))