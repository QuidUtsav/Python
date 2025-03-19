import random

# NUmber guessing game

def guess_num():
    
    secret_num= random.randint(1,100)
    
    print("Enter your guess from 1 to 100: ")
    attempt=0
    while True:
        try:
            guess=int(input("Your guess: "))
            attempt+=1
            if guess == secret_num:
                print(f'You got it!!!🥳🥳in {attempt} tries')
                break
            elif guess>secret_num:
                print("Higher than secret number")
            else:
                print("Lower than secret number")
        
        except ValueError:
            print("Value error")
            break
            
    choice=input("yes for playing again else enter any key: ").lower()
    if(choice=='yes'):
        guess_num()
guess_num()
