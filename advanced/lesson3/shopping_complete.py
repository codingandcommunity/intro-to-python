'''
A program to read and write from a shopping list file.
'''
FILE = 'list.txt'

while True:
    print("Would you like to (1) view shopping list, (2) add an item, (3) remove an item, or (4) quit?")
    choice = input("Choice: ")

    if choice == '1':
        # TODO Simply print all items in list.txt to the screen
        print("Items in the shopping list: ")
        with open(FILE, 'r') as file:
            for line in file:
                print('-\t' + line)
    elif choice == '2':
        # Get an input item from the user and append to the shopping list
        add = input("What item to add? ")
        with open(FILE, 'a') as file:
            file.write(add + '\n')
    elif choice == '3':
        # Get an item to remove from the user
        remove = input("What item to remove? ")
        
        # TODO Read all items from the shopping list
        items = []
        with open(FILE, 'r') as file:
            for line in file:
                items.append(line.strip())
        

        # TODO Write all items back into the shopping list if they are not
        #   the item to be removed
        with open(FILE, 'w') as file:
            for item in items:
                if item != remove.strip():
                    file.write(item + "\n")
    elif choice == '4':
        print("Goodbye!")
        break
    else:
        print("Unrecognized choice.")
    print()