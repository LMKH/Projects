#here i store the txt file in a variable then i open it
file_name = 'reg_form.txt'
file = open(file_name)

#below takes the opened file it and writes to it.
#then it prompts the user to input the amount of students registering for the exam.
#then a message appears once the user has inputted both pieces of infomation
#with a dotted line for the user to sign upon

with open(file_name, 'w') as file:
    studens_amount = int(input("Please enter the number of students who are registering for this exam: "))
    student_sign = ("Please sign your name: .................................." + "\n")

    for i in range(studens_amount):
        student_id = input("Please enter your student ID Number: ")
        print(student_id)
        file.write(student_id + "\n")
        file.write(student_sign)

#the for loop uses the range index inputted by the user on line 11.
#this then promts the user to input their student ID for however many times/students.
#finally it writes both the students ID and the place for them sign in the txt file