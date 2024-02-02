name = input("what is your name? ")
age = input("how old are you? ")
try:
    age = int(age) #convert string to integer
    birth_year = 2024 - age
    print(name, ", you were born in ", birth_year, ".", sep="")
    number = input("give me a number to divide the age ")
    number = int(number)
    print(age / number)

except ValueError:
    print("Invalid age, please enter a number.")
except ZeroDivisionError:
    print("you cannot divide by zero")
except:
    print("some other error i did not forsee")
else:
    print("no exceptions were raised.")
finally:
    print("thank you for playing")

