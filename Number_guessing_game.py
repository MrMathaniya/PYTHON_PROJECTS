from random import randint
no=randint(1,10)
guess=int(input("Guess a number between 1 and 10: "))
if guess==no:
    print("You guessed right!, The number was",no)
else:
    print("Opps! You guessed wrong, The number was",no)