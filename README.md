# Menu
***
This programme simply asks the user to input 3 food dishes of their choice. It will then print out neatly and clearly what they have chosen. This can be used when you need a simple choice menu.

# Methods
***
.replace(), .upper(), .strip().
Here I show my knowledge of using different methods to change strings. The examples are: using .replace(), I can replace all instances of "!" with a space, using .upper to convert a lowercase string to uppercase, and I use range and -1 to print the string in reverse. The following part shows how using the .strip() method can easily take all unwanted characters out of a string.

# Full Name
***
Programme that asks the user to input their name. If the name is too short for example an error message will be printed. Equally, if the name is too long, larger than 25 characters another error message will be printed. Plus an error message if the user hasn't inputted anything. If everything is correct, it will print a welcome message. This code can be implemented for things such as online forms, site logins etc.

# Logical Programming
***
Here I have created a programme that calculates and displays a user's input against a table of awards. This scenario is for a triathlon. Whatever time the user inputs, it will have a corresponding award. I have used arithmetic operations to calculate the totals. Simply input your hypothetical time in minutes and it will print out what award you would/would not have received. This code can be changed and implemented for other uses. E.g. when you need to calculate amounts or times within certain criteria.

# Finance Calculator
***
I first import math. The programme asks the user if they would like to calculate for an Investment or a Bond. If they choose Investment the programme will ask for inputs such as the amount they would like to deposit, what the interest rate is, and how many years they plan on investing. Following on from these inputs, the user is asked for either a 'simple' or 'compound' input. For simple: The deposit is multiplied by the interest rate / 100 and then multiplied by the number of years. For compound: Math.pow is used in this calculation. (X raised by the power of Y) The deposit multiplied, interest rate / 100 * years again. For Bond it is the same sort of question, but with a different calculation.

# While Loop
***
The user inputs their number of choice, it will be stored and added up as the loop continues to ask the user to input more numbers. Once the user is done adding numbers, they just have to input -1. This will exit the while loop and will calculate the average and the user's number.

# For Loop
***
I use a for loop alongside the range() function to loop through (0,5). With this, I have the programme print out stars. Once it reaches the end of the range: 5, it stops and the outcome is a starry design on 5 lines with 5 stars each.

# Calculator
***
My calculator programme starts by opening and writing all information inputted like the total to a file. First, the user is prompted to input the first number. There are failsafes throughout this programme that will catch errors from the user, e.g. inputting a letter instead of a number will cause an error. Then the user must input a second number. Once both are done, the user will be asked which operator they would like to use: "+" - addition, "-" subtraction, "/" divide, "*" multiplication. They must use the correct corresponding key for the programme to run. Finally, the total will print.

# Alternative
***
This programme outputs 2 strings. One with individual characters with upper & lower case letters. One with individual words with upper & lower case letters. The user can input whatever sentence they like and the output will show 2 different variations of that sentence.

# Cafe
***
In this programme I use dictionaries and lists to work out the amount of stock a cafe has and how much money it will cost. I use a for loop to work out the stock * by the price. Then it prints out the cost with a £ sign.

# Student Register
***
Here is a student register. Firstly, the user will be prompted to input exactly how many students will be taking a test. Once they have done this, they then need to input the students' ID number. If they selected 3 for example in how many students there are, they would have to input 3 student ids. It takes the input and uses range() to keep it within that range whilst the for loop runs. When it has reached the number inputted it will stop. On the file, it will print and show the students' ID number alongside a dotted line for them to sign upon.
