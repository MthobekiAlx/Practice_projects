# first step receive input from the user
ceaser_string = input("Enter characters to hide: ")

# store said input
secret_cstring = ""

# receive unit to shift with
shift_value = eval(input("Please enter the number to shift between 0 and 26: "))

shift_value = int(shift_value)

print("Shift value is: ", shift_value)

# maybe im thinking about it too hard, but we check if we are adding or subtracting
operator = input("Enter '+' or '-' for encryption: ")

# Assuming ceaser_string is defined before this snippet
if ceaser_string.isupper():
    for char in ceaser_string:
        secret_cstring += str(ord(char))
    num = int(secret_cstring)  # Convert the entire string to an integer

    if operator == "+":
        new_cstring = ""
        for i in range(0, 13):  # Loop through the range of shift values
            new_cstring_value = num + i
            char_code = str(new_cstring_value)
            new_cstring += char_code
            ceaser_string = ""
            i = 0
            while i < len(new_cstring):
                char_pair = new_cstring[i:i+2]  # Get a pair of numbers from the code
                ceaser_string += chr(int(char_pair))  # Convert the pair of numbers back to a Unicode character
                i += 2  # Move to the next pair of numbers

# Print the modified ceaser_string
print("Modified ceaser_string:", ceaser_string)




my else statement

else: #works for both upper and lower and the combination of 
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
        print("Error input, try again")
