'''
File I/O exercises.
'''

'''
# 1. Write a loop to write each string in the list
#      to the file.

# To make a new line, use '\n' e.g. file.write('foo\n')

to_write = ["All", "my", "favorite", "things"]
with open('write.txt', 'w') as file:
    # Your code here

print("Finished exercise 1")
'''

'''
# 2. Read each line from read.txt and print its length
#      on screen.
# Expected output:
# ---------------------
# 2
# 3
# 4

with open('read.txt', 'r') as file:
    # Your code here

print("Finished exercise 2")
'''

'''
# 3. Write each line that starts with an 'a' in mix.txt
#      to only_a.txt

# Remember, make a new line by adding '\n' e.g. file.write(line + '\n')

to_write = []
with open('mix.txt', 'r') as file:
    # Your code here
'''

# Don't modify this code, it checks your work in exercise 3.

success = True
line_seen = False
with open('only_a.txt', 'r') as file:
    for line in file:
        line_seen = True
        if line[0] != 'a':
            success = False
            break

if success and line_seen:
    print("Exercise 3 correct and finished!")
else:
    print("Something not right with exercise 3...")