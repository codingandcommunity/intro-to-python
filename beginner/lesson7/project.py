'''
Your task is to create a funcion that takes a string and turns it into a caesar cypher.
If you do not know what a caesar cipher is, here's a link to a good description:
https://learncryptography.com/classical-encryption/caesar-cipher
'''

def makeCipher(string, offset):
    # Your code here
    return string

s = input("Enter a string to be turned into a cipher: ")
o = input("Enter an offset for your cipher: ")
cipher = makeCipher(s, o)
print("You're new cipher is: %s".format(cipher))
