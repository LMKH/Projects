name = input("Please enter your full name: ")

#incase nothing has been printed
if name == "":
    print("You haven't entered anything. Please enter your full name")

#incase less than/equal 4 letters have been entered
elif len(name) <= 4:
    print("You have entered less than 4 characters. Please enter your full name")

#incase more than/equal 25 letters have been entered
elif len(name) >= 25:
    print("You have entered more than 25 characters. Please only enter your full name")

else:
    print("Thank you for entering your name")