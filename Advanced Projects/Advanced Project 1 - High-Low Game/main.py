import random
status = ""
i = 1
score = 0

print("--------------------------------")
print("Welcome to the High-Low Game!")
print("--------------------------------")

while(status != "lose"):
    print(f"\nRound: {i}")
    print(f"Your Score: {score}")
    you = random.randint(1, 100)
    computer = random.randint(1,100)
    print(f"Your number is: {you}\n")
    choice = input(("Do you think your number is 'higher' or 'lower' than computer's number?: "))

    if(((choice.lower() == "higher") and (you > computer)) or ((choice.lower() == "lower") and (you < computer))):
        print(f"You were Correct! The computer's number was: {computer}")
        status = "win"
        score +=1
        i += 1
    
    else:
        print(f"Aww, that's Incorrect. The computer's number was {computer}")
        status = "lose"

print(f"\nYour Score is: {score}\n")