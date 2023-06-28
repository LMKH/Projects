sentence_1 = "The!quick!brown!fox!jumps!over!the!lazy!dog"
sentence_2 = "The quick brown fox jumps over the lazy dog"
sentence_3 = "The quick brown fox jumps over the lazy dog"

#1 - replaces "!" with an empty space
#2 - makes the sentance all upper case
#3 - prints the string in reverse

print(sentence_1.replace("!", " "))
print(sentence_2.upper())
print(sentence_3[::-1])

#hero variable with the superman string surrounded by dollar signs
#to remove the dolar signs i used the .strip function and 
#in the parentheses i put the dollar signs. this tells the programme to remove
#all instances of a dollar sign. the print function prints the result, superman without the $
hero = "$$$Superman$$$".strip("$$$")
print(hero)