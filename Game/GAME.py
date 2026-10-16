# stone paper scissor 
#-1 for the stone 
#0 for the paper 
#1 for the scissor 
import random
while True:
        
    computer = random.choice([-1, 0, 1])
    youstr = input("Enter your choice (s=stone, p=paper, c=scissors): ").lower()
    youDict = {"s": -1, "p": 0, "c": 1}
    you = youDict[youstr]
    if computer == you:
        print("NO one won")
    if computer == 1 and you == -1:
        print("You won ")
    elif computer == -1 and you == 1:
        print("comp won ")
    elif computer == 1 and you == 1:
        print("no one won ")
    elif computer == 0 and you == -1:
        print("comp won ")
    elif computer == -1 and you == 0:
        print("You won ")
    elif computer == 0 and you == 0:
        print("no one won ")
    elif computer ==0 and you == 1:
        print("You won")
