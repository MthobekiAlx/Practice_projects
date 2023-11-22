"""
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

#more notes
letter_z = "z"
num_3 = "3"
a_space = " "
num4 = "3.14"
    #operations
print("Is z a letter or a number: ", letter_z.isalnum())
print("Is z a letter: ", letter_z.isalpha())
print("Is 3 a number: ", num_3.isdigit())
print("Is z a lower: ", letter_z.islower())
print("Is z a uppercase: ", letter_z.isupper())
print("Is space a space: ", a_space.isspace())

def isfloat(str_val): #its a function defination meaning that we created a function so as to make the code easier to understand as opposed to calling it again and again
    try:
        float(str_val)
        return True
    except ValueError:
        return False # from try to except is all part of exception handling as to check whether set input is true or not
print("is pi a float: ", isfloat(num4))

word = "Wrong"
if word.isupper():
    print("true")
else:
    print("false")
"""

# fuctions notes
"""
 def assign_name():
    name = "Doug"

assign_name()

print(name) # means that anythimg defined within a fuction is not available everywhere




def change_name(name):
    name = "Mark"

name = "Tom"

change_name(name) 

print(name) # what was taken was the global name not the one defined in the fuction

def change_name(name):
    return "Mark"

name = "Tom"

name = change_name(name) 

print(name) # one way to use the defined function

"""
