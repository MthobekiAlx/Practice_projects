# Age importance example
# 1 - 18 --> important
# 21, 50 and >65 --> important
# All others not important

# Recieve age input
age = eval(input("Enter age: ")) #eval fuaction automatically converts strings to integer

# and: if both are true
# or: if either is true then its true
# not: converts a true condition into a false one

# if age is both greater than or equal to 1 and less than or equal to 18 then its important
if (age >= 1) and (age <= 18):
    print("Important")

# if age is either 21 or 50 then important
elif (age == 21) or (age == 50):
    print("Important")

# we check if age is less than 65 and then convert true to false and vice versa
elif not(age < 65):
    print("Important")

# Else not important
else:
    print("Not an important age")