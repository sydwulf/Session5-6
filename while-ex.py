import random
# play a dice game with 3 lives, 6 wins the game

lives = 3
while lives > 0:
    print("you have", lives, "lives left.")
    # roll the dice
    dice = random.randint(1,6)
    print("you rolled a", dice)
    # check if you win
    if dice == 6:
            print("\n\nYOU WIN!\n\n")
            break
    else: # this is not necessary due to the break, as if the code gets this far it means that the number is not 6
     lives = lives -1
else:
    print("YOU LOSE")



print ("thank you for playing. Goodbye.")