from random import randint
no=randint(1,10)
guesses=0

while True:
    guess=int(input("Guess a number between 1 and 10: "))
    guesses+=1
    if guess==no:
        print("You guessed right!, The number was",no)
        break
    else:
        # print("Opps! You guessed wrong, try again")
        if guess>no:
            print(f"The number is small than {guess}")
        else:
            print(f"THe number is greater than {guess}")

print(f"you've guessed the number in {guesses} guesses!")