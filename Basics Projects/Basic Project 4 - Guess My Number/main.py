import random
n = random.randint(0,99)

a = -1
guessess = 1

while(a != n):
    a = int(input("Guess the Number: "))
    if(a < n):
        print("Higher Number Please!")
        guessess += 1

    if(a > n):
        print("Lower Number Please!")
        guessess += 1

print(f"Congratulations! You have Sucessfuly guessed the Number {n} in {guessess} attempts.")