import random
nlist = [random.randrange(1,101) for x in range(1, 101)]
print(nlist)
nlist.append(100)
# the search term is the number in the list that the linear search is looking for
searchTerm = int(input("Enter a number you'd like to search for: "))
# flag
found = False
# count is how many times the number you're looking for is in the list
count = 0
# Loops through all of the data elements in the list
for x in range(len(nlist)):
    # if the search term is in the list then found is true
    if (searchTerm == nlist[x]):

        found = True
        count = count + 1
# since found = true, it will tell you that the number you're looking for has been found, and how many times it has been found
if (found == True):

    print("Data has been found", count, "times")
else:
    print("Data has not been found")
# if the number you're searching for hasn't been found, it'll perform an else statement and tell you that your data hasn't been found
