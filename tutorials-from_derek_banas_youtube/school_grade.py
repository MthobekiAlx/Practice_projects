# If age is 5 go to kindergarten
# Ages 6-17 goes to grade 1-12 respectively
# if age is gretaer than 17 goes to college
# complete in 10 lines or less

# ask for age input
age = eval(input("How old are you?: "))

# Handle if age is 5 and less
if age <= 5:
    print("Go to kinderdarten")

#handle if age is 6-17
elif age ==6 or age <=17:
    grade = age - 5
    print("Go to grade", format(grade))

# Handle if age is greater than 17
else:
    print("Go to college")
