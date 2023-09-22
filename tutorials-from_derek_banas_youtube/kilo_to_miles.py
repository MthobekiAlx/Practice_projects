#receive miles and convert to kilometers
num1 = input("Enter miles: ")

#convert string to regular num integer
num1 = int(num1)

#strore 1.60934 into integer number
num2 = 1.60934

#kilometers to miles operation
kilometers = num1 * num2

#print out results
print("{} * {} = {}".format(num1, num2, kilometers))