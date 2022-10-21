import random
num = random.randint(1,20)
print(num)  
numGuesses = 0

for i in range(1,21):
    guess = input("Guess the number between 1/20: ")
    if numGuesses < 10:
        if int(guess) != num:
            print(f"Incorrect {guess} is not right try again")
            numGuesses += 1
        else:
            print(f"Correct the answer was {num}, you got the answer in {numGuesses+1} tries!")
            break
    else:
        print("You failed")
        break