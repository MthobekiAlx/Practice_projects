while True:
    samp_stirng = input("Enter a message you like to hide: ")
    secret_string = "" 
    error_flag = False

    for char in samp_string:
        if 'A' <= char <= 'z':
            secret_string += str(ord(char))
            else:
                print("Error the message you enetered is not recognised")
                error_flag = True
                break 
    if not:
        print("Secret message is: ", secret_string)
        break

        
