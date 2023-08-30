import art
import random
numbers=[]
guesses=0

for i in range(1,101):
    numbers.append(i)
computers_choice=random.choice(numbers)
def compare(user_guess, computers_choice):
    
    if computers_choice==user_guess:
        return "You win"
    
    elif computers_choice>user_guess:
        return "Too low"
    elif computers_choice<user_guess:
        return "Too high"
print(art.logo)
print("Welcome to the number guessing game!")
print(f"I'm thinking of a number between {numbers[0]} and {numbers[99]} " )


level=input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
if level=="easy":
    guesses=10
elif level=="hard":
    guesses=5
else:
    print("Invalid input")
    exit()


while guesses > 0:
    print(f"You have {guesses} attempts remaining to guess the number")
    user_guess = int(input("Make a guess: "))

    result = compare(user_guess, computers_choice)
    print(result)

    if result == "You win":
        break

    guesses -= 1

if guesses==0:
    print(f"Sorry you have run out of guesses, the correct number was {computers_choice}")