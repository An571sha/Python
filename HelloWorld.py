from random import randint
answer = randint(1,10)
guess = int(input("Guess a number between 1 and 10:"))
number = False
while(number):
    if(guess<answer):
        print("go higher")
    elif(answer>guess) :
        print("go lower")
    else:
        print("correct")
        number =True
    
