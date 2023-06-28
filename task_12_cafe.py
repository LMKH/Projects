#here is the menu items. in a list format.
menu_items = ["Spam", "Ham", "Eggs", "Bacon"]

#here is the menu items stock. The numbers next to each item show the amount left in stock.
#dictonary
stock = {
    "Spam": 32,
    "Ham": 27,
    "Eggs": 48,
    "Bacon": 50,
}

#the numbers indicate the prices for each menu item. another dictionary.
price = {
    "Spam": 3,
    "Ham": 2,
    "Eggs": 1,
    "Bacon": 4,
}

# i store the current total as 0
total = 0

#for loop will iterate through the menu_items
#then it will check what the stock amount and price of those menu items are.
#the output is then printed and updates the total

for i in menu_items:
    total += stock[i] * price[i]

#this f string displays the total of the 4 items with a £ sign    
print(f'The total of all 4 items is £{total}')