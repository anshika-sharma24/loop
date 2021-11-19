



guess=int(input("enter your number"))
i=0
chance=4
while(i<5):
    user=int(input(" enter your guess number"))
    if(guess==user):
        print("you win this game")
        break
    else:
        print("you have",chance ,"chance")
    i=i+1
    chance-=1
# print(" sorry you have only five chance")