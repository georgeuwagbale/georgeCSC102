import random

lives = 2
score = 0
while lives != 0:

    comp_guess = random.randrange(1, 20)
    print(comp_guess)

    trial = 3
    while trial != 0:
        print("Trial = ", trial)
        user_guess = int(input("Guess a number: "))
        if comp_guess == user_guess:
            score += 2
            print("Next level >>")
            break
        elif comp_guess > user_guess:
            print("Number too high, try again")
        elif comp_guess < user_guess:
            print("Number too low, try again")
        lives -= 1
        trial -= 1
