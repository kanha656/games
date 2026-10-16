import random
n = random.randint(1,100)
a = -1 
guesses = 0
while(a != n):
    guesses +=1 
    a = int(input("Guess the number : ") )
    if (a>n):
       print("low number")
    else:
       print("high number")
print(f"you have gueese the number in this guesses{guesses} attempts")