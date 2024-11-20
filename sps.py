import random

#user input
p = int(input("Enter 1 for stone, -1 for paper, 0 for scissor: "))


if(p==1 or p==-1 or p==0):
    #computer choice
    c = random.randint(-1,1)
    if c == 1:
        print("computer chose stone")
    elif c == 0:
        print("computer chose scissor")
    elif c==-1:
        print("computer chose paper")

    #game logic
    if p == c:
        print("draw")
    elif p == 1 and c == 0:
        print("you win")
    elif p == 0 and c == -1:
        print("you win")
    elif p == -1 and c == 1:
        print("you win")
    else:
        print("you lose")

else:
    print("Invalid input")
