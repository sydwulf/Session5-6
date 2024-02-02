name = input("what is your name? ")
age = input("how old are you? ")
#print("Hello,", name, "!", sep="")
#comma adds space by default, + connects them
#or: add seperator and make it = nothing
#brth_year = 2024 - age
#i can not do math with a number and a string as the age i write is not considered a number
age=int(age)
birth_year = 2024 - age
print(name, ", you were born in ", birth_year, ".", sep="")

