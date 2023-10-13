#Enter a string to hide in uppercase: HIDE
samp_string = input("Enter a string message to hide: ")

#before we store our secret message string
secret_string = ""

# cycle through each character in the string
for char in samp_string:
    secret_string += str(ord(char)) #stores each character code in new string

print("Secret message is: ", secret_string) #prints the secret message in code

#cycle through each character code 2 numbers at a time since the assigned values come in pairs from 65-90 and we need to seperate them back pairs
samp_string = ""
for i in range(0, len(secret_string)-1, 2):
    char_code = secret_string[i] + secret_string[i+1] #get the 1st and 2nd numbers of ecah respective pair from code
    samp_string += chr(int(char_code)) #convert code back to the string message

print("The original message is: ", samp_string)