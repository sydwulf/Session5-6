import random

drinks = ["vodka", "tequila", "rum", "gin", "beer", "seltzer", "wine", "whiskey"]
try:
    name = input("What is your name? ")
    age = input("How old are you? ")
    age = int(age) # convert string to integer
    country = input ("where are you from? ")
except ValueError:
    print("Invalid age. Please enter a number.")
else:
    if age < 0 or age > 140
        print("You are not human. This game is for humans")
    elif age > 120:
        print("You are too old to play the awesome drinking game")
    #now we have a good age to play with
    elif age < 18:
        print("You are a minor. You can not play the awesome drinking game.")
    elif (country == "USA" or country == "UAE") and age > 21:
        print("you are not allowed to drink in the USA or UAE")
    else:
        print("You are an adult. You can play the awesome drinking game.")
        print("Have some", random.choice(drinks), "and enjoy the game.")