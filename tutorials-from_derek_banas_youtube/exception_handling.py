while True:
    try:
        number = int(input("Please enter a number: "))
        break

    except ValueError:
        print("please eneter a number")
    
    except:
        print("An unkown error occurred")

print("Thank you for entering a number")
