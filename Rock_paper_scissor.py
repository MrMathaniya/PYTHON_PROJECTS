import random

user_score=0
comp_score=0


options=["rock","paper","scissor"]
comp_op=random.randint(0,2)


print("Do you want to play Rock/paper/scissors ")
q=input("Enter here:")
if q.lower()=="yes":
    print("Well here we go.")
elif q.lower()=="no":
    print("Well see you again Goodbye.")
    exit()
else:
    print("type yes or no only.")
    exit()


while True:

    user_pick=input("Type your choice from rock/paper/scissor OR {q} to quit:-").lower()
    if user_pick=="q":
        break
    if user_pick not in options:
        continue


    comp_pick=options[comp_op]
    print("Computer picked",comp_pick)
    if user_pick=="rock" and comp_pick=="scissor":
        print("You won!")
        user_score+=1
    elif user_pick=="paper" and comp_pick=="rock":
        print("You won!")
        user_score+=1
    elif user_pick=="scissor" and comp_pick=="paper":
        print("You won!")
        user_score+=1
    else:
        print("You lost!")
        comp_score+=1

        # quit=input("Do you want to quit? (yes/no)").lower()
        # if quit=="yes":
        #    print(f"You're score {user_score} and computer score {comp_score}")
        #    exit()

print(f"You're score {user_score} and computer score {comp_score}")
if user_score>comp_score:
     print("You won!")
elif user_score<comp_score:
      print("You lost!, Computer won!")
else:
     print("DRAW!!")
