import random # Imports random numbers

items = [random.randint(0, 1000) for i in range(1000)] # all numbers between 1-100

random.shuffle(items) # Shuffles the 100 numbers into a random order

SearchTerm = int(input("Enter a number you'd like to search for: ")) # Allows the user to input a number to find in the list
found = False
count = 0

for x in range(0, len(items)): # Loops through every number in the list
    if (SearchTerm == items[x]): # checks to see if the number has been found in the list
        found = True
        count = count + 1


if (found == True):
    print("Item found", count, "times")
else:
    print("Item not found")
