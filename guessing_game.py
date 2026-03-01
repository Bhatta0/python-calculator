import random

def generate_number():
    return random.randint(1, 100)

def get_guess():
    while True:
        try:
            guess = int(input("Enter your guess (1-100): "))
            return guess
        except ValueError:
            print("Invalid input. Please enter a number.")

def check_guess(guess, secret):
    if guess < secret:
        return "Too low!"
    elif guess > secret:
        return "Too high!"
    else:
        return "Correct!"

def get_difficulty():
    print("\nSelect Difficulty:")
    print("1. Easy   — Unlimited guesses")
    print("2. Medium — 10 guesses max")
    print("3. Hard   — 5 guesses max")
    
    while True:
        choice = input("Enter 1, 2 or 3: ")
        if choice == "1":
            return None  # unlimited
        elif choice == "2":
            return 10
        elif choice == "3":
            return 5
        else:
            print("Invalid choice. Enter 1, 2 or 3.")

def play_game():
    print("=== Number Guessing Game ===")
    
    max_guesses = get_difficulty()
    secret = generate_number()
    attempts = 0

    while True:
        # check if guess limit reached
        if max_guesses is not None and attempts >= max_guesses:
            print(f"\nGame Over! You ran out of guesses.")
            print(f"The secret number was: {secret}")
            break

        guess = get_guess()
        attempts += 1
        result = check_guess(guess, secret)
        print(result)

        # show remaining guesses if limited
        if max_guesses is not None and result != "Correct!":
            remaining = max_guesses - attempts
            print(f"Guesses remaining: {remaining}")

        if result == "Correct!":
            print(f"You got it in {attempts} attempts!")
            break

def main():
    while True:
        play_game()
        again = input("\nPlay again? (yes/quit): ")
        if again.lower() == "quit":
            print("Thanks for playing. Goodbye!")
            break

main()