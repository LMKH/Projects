#i define city_stay, which is the destination & take the city_price and put that with the users_choice
#same process for city_addition which takes the users_choice for how many days their staying and multiplies it by £150
#same process for city_rent which takes the users_choice for how many days they plan on renting a car & times it by £70
#then i take all the functions in holiday_total and add them up together.

def city_stay(user_choice): 
    total = city_price[user_choice]
    return total 

def city_addition(user_choice): 
    total = user_choice * 150
    return total

def city_rent(user_choice):
    total = user_choice * 70
    return total

def holiday_total(choice_a, choice_b, choice_c):
    total = city_stay(choice_a) + city_addition(choice_b) + city_rent(choice_c)
    return total

#here i store the city_flight destinations in a dictionary. For ease i have coded each city with a letter,
#this means it is more user-friendly as the user just has to input the letter specified to each city.
#city_price has the corrosponding cities price

city_flight = {
    "M": "Manchester, England",
    "P": "Paris, France",
    "B": "Berlin, Germany",
    "R": "Reykjavik, Iceland",
    "O": "Ottawa, Canada",
    "S": "Sydney, Australia",
    "T": "Tokyo, Japan",
    "G": "Glasgow, Scotland",
    "J": "Johannesburg, South Africa",
    "L": "Lisbon, Portugal",                        
    "N": "Nuuk, Greenland",
    "H": "Helsinki, Finland",
    "Q": "Quito, Ecuador",
    "C": "Cairo, Egypt",
}

if input in city_flight.keys():
    print(city_flight)

city_price = { 
    "M": 99,
    "P": 450,
    "B": 240,
    "R": 620,
    "O": 799,
    "S": 999,
    "T": 1050,
    "G": 49,
    "J": 799,
    "L": 199,
    "N": 420,
    "H": 360,
    "Q": 870,
    "C": 599,
}
for value in city_flight.values():
    print(value)

city_flight_choice = input("Where would you like to go? ").upper()

#above i ask the user to input the key, dosent matter if lower or upper case, as i use .upper()
#here i ask the user to input the number of nights they will be staying at a hotel. 
#i use int() so the user can only put a interger number. defensive. similar question below for rental

num_nights = int(input("How many nights are you going to be staying? "))

num_rental_days = int(input("How many days do you plan on renting a car? "))

#below i start calling my functions and printing them
#then finally i take all of the functions,
#print out a final message with the total cost for the holiday

flight_cost = city_stay(city_flight_choice)
print(flight_cost)

number_nights = city_addition(num_nights)
print(number_nights)

number_rental = city_rent(num_rental_days)
print(number_rental)

total_holiday = holiday_total(city_flight_choice, num_nights, num_rental_days)
print("The total cost of your holiday will be £" + (str(total_holiday)))