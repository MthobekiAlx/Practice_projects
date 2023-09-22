#Enter calculation: i.e 5 * 6

#store the user input of 2 numbers and the operator
num1, operator, num2 = input("Enter calculation").split()

#convert the string into integer
num1 = int(num1)
num2 = int(num2)

#if + then provide an output on addition
#print out results
if operator == "+":
    print("{} + {} = {}".format(num1, num2, num1+num2))
elif operator == "-":
    print("{} - {} = {}".format(num1, num2, num1-num2))
elif operator == "*":
    print("{} * {} = {}".format(num1, num2, num1*num2))
elif operator == "/":
    print("{} / {} = {}".format(num1, num2, num1/num2))
else:
    print("wrong operator input")
