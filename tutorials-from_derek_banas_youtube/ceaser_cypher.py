#Create a program that cyphers or hides the message inserted using char unit code shift
#Use isupper to decide which unit codes to work with - exception handling
#Add the key number of characters to shift -input from user
#check if the key is bigger or smaller than the unicode
# increase or decrese by max 26

#first step recieve input from the user
ceaser_string = input("Enter character to hide: ")

# Store the input string
secret_cstring = ""

# Receive the number to shift by
shift_num = int(input("Please enter the number to shift between 1 and 12: "))
print("num is: ", shift_num)

# Receive the operator (+ or -)
operator = input("Enter '+' or '-' for encryption : ")

# Use isupper to check which Unicode to work with
if ceaser_string.isupper():
    for char in ceaser_string:
        secret_cstring += str(ord(char))
        num = secret_cstring
        num = int(num)
        if operator == "+" and 1 <= shift_num <= 12:
            new_cstring_value = num + shift_num
            new_cstring = new_cstring_value
            new_cstring = str(new_cstring)

            ceaser_string = ""
            for i in range(0, len(new_cstring)-1, 2):
                char_code = new_cstring[i] + new_cstring[i+1]
                ceaser_string += chr(int(char_code))
#I think that I should do one for lower using islower and then do one for both so the second one should be an elif statement
elif ceaser_string.islower():
    for char in ceaser_string:
        secret_cstring += str(ord(char) - 22)
        num = secret_cstring
        num = int(num)
        if operator == "+" and 1 <= shift_num <= 12:
            new_cstring_value = num + shift_num
            new_cstring = new_cstring_value
            new_cstring = str(new_cstring)

            ceaser_string = ""
            for i in range(0, len(new_cstring)-1, 2):
                char_code = new_cstring[i] + new_cstring[i+1]
                ceaser_string += chr(int(char_code) + 22)
        elif operator == "-" and 1 <= shift_num <= 12:
                new_cstring_value = num - shift_num
                new_cstring = new_cstring_value
                new_cstring = str(new_cstring)

            ceaser_string = ""
            for i in range(0, len(new_cstring)-1, 2):
                char_code = new_cstring[i] + new_cstring[i+1]
                ceaser_string += chr(int(char_code) + 22)
    #I think that the problem is that the lower case subtracts a number then I'll have to make it work for the shift_num range
    #so I will do one for lower case letters only and run it
'''else: #works for both upper and lower and the combination of 
    if operator == "+" and 1 <= shift_num <=26: #I will have to change the shift range back to 1-12 since it covers the entire range
        for char in ceaser_string:
            secret_cstring += str(ord(char) -22) #get a number that puts it back and shift it by max 12
            num = secret_cstring
            num = int(num)
            if operator == "+" and 1 <= shift_num <= 26:
                new_cstring_value = num + shift_num
                new_cstring = new_cstring_value
                new_cstring = str(new_cstring)

            ceaser_string = ""
            for i in range(0, len(new_cstring)-1, 2):
                char_code = new_cstring[i] + new_cstring[i+1]
                ceaser_string += chr(int(char_code) + 22) #this puts it back meaning that I'll have to sort my initial ascii range

    elif operator == "-" and 1 <= shift_num <=26:
        for char in ceaser_string:
            secret_cstring += str(ord(char) - 22)
            num = secret_cstring
            num = int(num)
            if operator == "-" and 1 <= shift_num <= 26:
                new_cstring_value = num - shift_num
                new_cstring = new_cstring_value
                new_cstring = str(new_cstring)

            ceaser_string = ""
            for i in range(0, len(new_cstring)-1, 2):
                char_code = new_cstring[i] + new_cstring[i+1]
                ceaser_string += chr(int(char_code) + 22)

    else:
        print("Error input, try again")''''

print("The new message is: ", ceaser_string)



