#Enter a string in lower case to hide 
lower_string = input("Enter a string message to hide: ")

#store the secret code
secret_message =""

#cycle through each character in string
for char in lower_string:
    secret_message += str(ord(char))#stores each char as a string

print("secret message is: ", secret_message)#print secret message 

lower_string = ""
for i in range(0, len(secret_message)-1, 3):
    char_code = secret_message[i] + secret_message[i+1] + secret_message[i+2]
    lower_string += chr(int(char_code)) #convert code back to the string message

print("The original message is: ", lower_string)

#wrong code cause a to some other alphabet is out of ramge since its defined by three and not my pairs