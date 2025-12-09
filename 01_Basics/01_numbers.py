import random

List1 = [1, 2, 3, 4, 5]
List2 = ['apple', 'banana', 'cherry', 'date', 'elderberry']

print(random.choice(List1))
print(random.choice(List2))


# Create a simple number guessing game
number_to_guess = random.randint(1, 100)
countAttempt = 0
maxAttempt = 10

while countAttempt < maxAttempt:
    user_guess = int(input("Guess a number between 1 and 100: "))
    countAttempt += 1
    if user_guess < number_to_guess:
        print("Too low!")
    elif user_guess > number_to_guess:
        print("Too high!")
    else:
        print(f"Congratulations! You've guessed the number {number_to_guess} in {countAttempt} attempts.")
        break