#The proper ceaser cypher


#recieve the message to encrypt and the number to shift with
message = input("enter message to encrypt: ")
key = int(input("how many chars to shift(10-26)"))

# prepare the secret message 
secret_message= ""

#cycle through each cahracter in the message
for char in message:
    if char.isalpha(): 
        char_code  = ord(char)
        char_code += key
        if char.isupper():
            if char_code > ord('Z'):
                char_code -= 26
                # if smaller than A then add 26
            if char_code < ord('A'):
                char_code += 26

        else:
            if char_code > ord('z'):
                char_code -= 26
            # if smaller than A then add 26
            if char_code < ord('a'):
                char_code += 26
    # convert code to letter and add to message
        secret_message += chr(char_code)
    else:
        secret_message += char
print("encrypted messsage: ", secret_message)    

# to decrypt 
key = -key

orig_message = ""

for char in secret_message:
    if char.isalpha(): 
        char_code  = ord(char)
        char_code += key
        if char.isupper():
            if char_code > ord('Z'):
                char_code -= 26
                # if smaller than A then add 26
            if char_code < ord('A'):
                char_code += 26

        else:
            if char_code > ord('z'):
                char_code -= 26
            # if smaller than A then add 26
            if char_code < ord('a'):
                char_code += 26
    # convert code to letter and add to message
        orig_message += chr(char_code)
    else:
        orig_message += char
print("decrypted messsage: ", orig_message)