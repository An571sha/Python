from random import randint
answer = randint(1,10)
number = False
while not(number):
    guess = int(input("Guess a number between 1 and 10:"))
    if(guess<answer):
        print("go higher")
    elif(answer>guess):
        print("go lower")
    else:
        print("correct")
        number =True
    
