#get the number of rows for the trees 
rows = input("Enter the height of the tree: ")
#or rows = eval(input("Enter the height of the tree: "))

#convert into integer
rows = int(rows)

#get the starting spaces for the top of the tree
spaces  = rows - 1

# There is one hash to start with the increment
hashes = 1

#save stump till later
stump_spaces = rows - 1

#make sure the right number of rows are printed
while rows != 0:


#print the spaces
    for i in range(spaces):
        print(' ', end="")

#print the hashes
    for i in range(hashes):
        print(' ', end="")

#newline after each row is printed
print()

#hashes increment by 2 each time
hashes += 2

#rows decrement each time and jump out the loop
rows -= 1

#print the spaces before the stump and then hash
for i in range(stump_spaces):
    print(' ', end="")

print("#")
