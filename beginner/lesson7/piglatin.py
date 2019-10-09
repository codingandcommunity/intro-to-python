'''
Write a function translate that translates a list of words to piglatin
ex) input = ['hello', 'world']
    output = ['ellohay', 'orldway']

remember, you can concactenate strings using +
ex) 'hello' + ' ' + 'world' = 'hello world'
'''

def translate(     ):
    # Your code here

phrase = (input("Enter a phrase -> ")).split() # takes a string as input and splits it into a list of strings; ex: hello world becomes ['hello', 'world']
piglatin = translate(phrase) # write the function translate
print(' '.join(piglatin)) # takes a list of strings and make them into one string with a space between each item; ex: ['hello', 'world'] becomes 'hello world'