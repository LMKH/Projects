import math

#keeps total
users_number = 0
count = 0
number_choice = 0

#keeps asking the user to input a number
while number_choice != -1:
    
#if number chosen is -1 or less it continues onto print the total of users number
    number_choice = int(input("Please enter your number of choice: "))
    count += 1

#adds the numbers up
    users_number += number_choice

average = users_number / count 

print(users_number)
print(math.ceil(average))