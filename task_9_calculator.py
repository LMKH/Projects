file_name = 'sample.txt'
input_file = open('sample.txt', 'w+')  

#both of these 'while True' statements ask the user to input a valid number. that can be either a float or intiger number.
#if the number inputted is fine it will 'break' and go on to ask for a second number. 
#if that number is fine to it'll go onto ask the user to input an operator.

#if the user does not input a valid number, such as a letter or nothing at all, 
#the 'except ValueError' will run and prompt the user to re-input a valid number. 
#it will ask them to input a valid number until they do. it will do this for both while True numbers.
while True:
    try:
        num_1 = float(input("Please enter a number: "))
        break
    except ValueError:
        print("This is not a valid number, please enter a valid number.")
    
while True:
    try:
        num_2 = float(input("Please enter a number: "))
        break
    except ValueError:
        print("This is not a valid number, please enter a valid number.")

#here is the operator variable. it will ask the user to input:
#a '+' for addition, a '-' for subtraction, a '/' for division, and a '*' for multiplication.
#once the user has inputted a valid option it will run. 
#'\n' just spaces them out better on new lines. more visably better & user friendly

operator = input("Please enter an operator: \n+ \n- \n/ \n* \n ")

if operator == "+":
    addition = (num_1 + num_2)
    print(num_1 + num_2)
    result = (num_1 + num_2)
    print(input_file)
    input_file.close()

elif operator == "-":
    subtraction = (num_1 - num_2)
    print(num_1 - num_2)
    result = (num_1 - num_2)
    print(input_file)
    input_file.close()

elif operator == "/":
    division = (num_1 / num_2)
    print(num_1 / num_2)
    result = (num_1 / num_2)
    print(input_file)
    input_file.close()

elif operator == "*":
    multiply = (num_1 * num_2)
    print(num_1 * num_2)
    result = (num_1 * num_2)
    print(input_file)
    input_file.close()

#here i use the if, elif and else functions.
#under each respected if & elif there is a print function,
#which will display the answer of the 2 numbers AND the chosen operator.

#similar to what I've done for the error handling in the while True statemnts, if the user does not input
#a valid option it will run the else clause and give a error message. 
else:
    print("You have not inputted a valid operator. Please try again.")