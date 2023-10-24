# this are note to be used as refremce to solve all the problems that are in this tutorial

#1-operations that can be carried out on a string of characters

rand_string = "  this is a random string" # example of the string

#operations
rand_string = rand_string.lstrip() #strips the space on the left 
rand_string = rand_string.rstrip()
rand_string = rand_string.strip() #removes all the spaces before and after a string

print(rand_string.capitalize())
print(rand_string.upper())
print(rand_string.lower())

a_list = ["Bunch", "of", "random", "words"]
print(" ".join(a_list))

a_list2 = rand_string.split()
for i in a_list2:
    print(i)

print("How many is :", rand_string.count("is"))
print("where is string :", rand_string.find("string"))
print(rand_string.replace(" a ", " a kind of "))