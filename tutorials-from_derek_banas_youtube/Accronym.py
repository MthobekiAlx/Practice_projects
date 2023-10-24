#Ask for user input
string_accro = input("Please enter a string message to be converted into an accroynm : ")

#convert the tring into uppercase
string_accro = string_accro.upper()
print(string_accro)

#convert the tring into a list
a_list1 = string_accro.split()

#cycle through the list
for word in a_list1:
    print(word[0], end="")

#get the 1st letter of the word and eliminate new line
print()