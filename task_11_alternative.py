#here is where i promt the user to input their sentence of choice
sentence = input("Please enter a sentence: ")

#this is for when my string gets updated. and it stores it.
updated_string = ""

# for the task, i need to loop through the sentence. this is why i use a for loop.
#i need the values of the sentence too, so i use len() for the lenghth of the sentence.
#along with range so i can loop/itterate throgh it to get the index values.

for i in range(len(sentence)):

#modulous to check for every second index.
#odd and even numbers, will change between both uppercase and lowercase.
#'updated_string' concatinates with the 'sentence'. 

    if i % 2 == 1:

        updated_string += sentence[i].upper()
    else:

        updated_string += sentence[i].lower()

print(updated_string)

#indexed by 'i', upper() for uppercase for even index numbers
#.lower() for odd index numbers
#the print(updated_string) prints the updated string.

#here i store the original sentence in a new variable 'new_sentence'
#for i in range(len(new_sentence)) runs similar to the original sentence above.
#only this time instead of going through individual characters,
#it loops through individual words, making them uppercase/lowercase depending on their index in the list.

new_sentence = sentence
new_sentence = new_sentence.split()

for i in range(len(new_sentence)):

    if i % 2 == 1:
        new_sentence[i] = new_sentence[i].upper()

sep = " "
print(sep.join(new_sentence))

#.split() splits the individual words up in a list,
# i then have to rejoin it so it's no longer in a list format, and instead just a string.
# i title a variable as 'sep' for seperator.
# then I add a space inside of it, so the programme knows to put a space inbetween the words.

# print(sep.join(new_sentence)) then finally puts all the pieces together joining the seperator with the new sentence. 

# this programme outputs 2 strings. 
# one with individual characters with upper and lowercase letters.
# one with indivdual words with upper and lowercase letters.