#i ask the user to input individual times.
#i've asked for it in minutes so it's more user-friendly.

swimming = (int(input("Please enter your time for Swimming in minutes: ")))
bike = (int(input("Please enter your time for Cycling in minutes: ")))
run = (int(input("Please enter your time for Running in minutes: ")))

# Here is the total of the three individual times/inputs. it displays the total time.
# i combined the variables into a variable so they can be added up.
# i used the str() function to combine the 'total variable' into a string sentance. converting it from a int() to a str()

total = (swimming + bike + run)
print("Your total time is " + str(total) + " minutes.")

# i use if, elif and else statements.
# the following is a if & elif statement, Here will show where the users 'total' has came.

if (swimming + bike + run) <= 100:
    print("You are within the qualifying time. \nYou have earned the 'Provincial Colours Award'.")
elif (swimming + bike + run >= 101 and swimming + bike + run <= 105):
    print("You are within 5 minutes of the qualifying time. \nYou have earned the 'Provincial Half Colours Award'.")
elif (swimming + bike + run >= 106 and swimming + bike + run <= 110):
    print("You are within 10 minutes of the qualifying time. \nYou have earned the 'Provincial Scroll Award'.")
else:
    print("You are more than 10 minutes late of the qualifying time. \nYou have earned nothing.")

# the first if statement checks to see if the users time is less than/equal to 100 mins.
# if not, it then passes to the first elif statement. Here i use the 'and' function, where it checks the user total & the time between 101 mins and 106 mins.
# if it doesn't pass that elif it moves onto the second elif statement. This checks if the time is within 106 mins and 110 mins.
# then if the user has gone over more than 10 minutes the else clause kicks in as its anything over 110 mins. 