#have the usuer enter their investment ammountand expected interest
#Each year their investment will increase by thier investment + their investment * interest rate 
#print out the results after a 10 year period
ammount = input("enter your investment ammount: ")
interest = input("enter expected interest: ")

#convert to float
ammount = float(ammount)

#convert to float
interest = float(interest) * 0.1

#perform the calculations
ammount = ammount + (ammount * interest)

print("your earned ammount after 10 years is: {:.2f}".format(ammount))
