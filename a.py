from random import randint
t = [1,2,3,4,5,6]
computer = t[randint(0,5)]
player=0
score=0
while 1:
    player = int(input("Enter your choice:1,2,3,4,5,6\n"))
    if (player == computer):
        print("You are OUT!")
        break
    else:
         score=score+player
    computer = t[randint(0,5)]
print("Your score is",score)
