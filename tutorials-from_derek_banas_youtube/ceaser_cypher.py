#Create a program that cyphers or hides the message inserted using char unit code shift
#Use isupper to decide which unit codes to work with - exception handling
#Add the key number of characters to shift -input from user
#check if the key is bigger or smaller than the unicode
# increase or decrese by max 26

#first step recieve input from the user
ceaser_string = input("Enter character to hide: ")

#store said input
secret_cstrinng = ""

#recieve unit to shift with
shift_num = eval(input("Please enter the number to shift between 0 and 26: "))

shift_num = int(shift_num)

print("num is: ", shift_num)

#maybe im thinking about it too hard but we check if we adding or subtracting
operator = input("Enter '+' or '-' for encryption : ")


#use isupper to check which unicode to work with
if ceaser_string.isupper():
    for char in ceaser_string:
        secret_cstrinng += str(ord(char))
    print("message before ecyripting is : ", secret_cstrinng)

    ceaser_string = ""
    for i in range(0, len(secret_cstrinng)-1, 2):
        char_code = secret_cstrinng[i] + secret_cstrinng[i+1] #get the 1st and 2nd numbers of each respective pair from code
        ceaser_string += chr(int(char_code)) 

else: #works for both upper and lower and the combination of 
    for char in ceaser_string:
        secret_cstrinng += str(ord(char) - 38) #stores each character code in new string
    print("Secret message is: ", secret_cstrinng) #prints the secret message in code
    
    ceaser_string = ""
    #cycle through each character code 2 numbers at a time since the assigned values come in pairs from 65-90 and we need to seperate them back pairs
    for i in range(0, len(secret_cstrinng)-1, 2):
        char_code = secret_cstrinng[i] + secret_cstrinng[i+1] #get the 1st and 2nd numbers of each respective pair from code
        ceaser_string += chr(int(char_code) + 38) #convert code back to the string message

        new_string = ceaser_string 
      

print("The new message is: ", new_string)


