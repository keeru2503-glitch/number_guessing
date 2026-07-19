import random

print("===== Number Guessing Game =====")

while True:
    # Difficulty Selection
    print("\nSelect Difficulty:")
    print("1. Easy (1-10)")
    print("2. Medium (1-50)")
    print("3. Hard (1-100)")

    while True:
        choice = input("Enter your choice (1/2/3): ")

        if choice == "1":
            max_number = 10
            break
        elif choice == "2":
            max_number = 50
            break
        elif choice == "3":
            max_number = 100
            break
        else:
            print("Invalid choice! Please enter 1, 2, or 3.")

    
    secret_number = random.randint(1, max_number)
    attempts = 0

    print(f"\nI have chosen a number between 1 and {max_number}.")
    print("Can you guess it?")

    # Guessing Loop
    while True:
        try:
            guess = int(input("Enter your guess: "))

            if guess < 1 or guess > max_number:
                print(f"Please enter a number between 1 and {max_number}.")
                continue

            attempts += 1

            if guess < secret_number:
                print("Too low! Try again.")
            elif guess > secret_number:
                print("Too high! Try again.")
            else:
                print(f"\nCongratulations! You guessed the number in {attempts} attempts.")
                break

        except ValueError:
            print("Invalid input! Please enter a valid number.")

    
    play_again = input("\nDo you want to play again? (y/n): ").lower()

    if play_again != "y":
        print("\nThanks for playing!")
        break