from random import randint
no=randint(1,10)
guesses=0
chances=5

while True:
    guess=int(input("Guess a number between 1 and 10: "))
    guesses+=1
    if guess==no:
        print("You guessed right!, The number was",no)
        break
    else:
        # print("Opps! You guessed wrong, try again")
        if chances==0:
            print("NO MORE CHANCES!\n YOU LOST!!!")
            exit()
        elif guess>no:
            print(f"The number is small than {guess}")
            chances-=1
            print(f"{chances} chances left!")
        elif guess<no:
            print(f"The number is larger than {guess}")
            chances-=1
            print(f"{chances} chances left!")
        else:
           exit()
if no==guess:
    print(f"you've guessed the number in {guesses} guesses!")
else:
    exit()