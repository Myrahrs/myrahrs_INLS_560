import random  # Import the random module to let the computer make random choices.

# Function to convert single-letter choice to full word.
def get_full_name(choice):
    if choice == 'r':
        return 'rock'
    elif choice == 'p':
        return 'paper'
    elif choice == 's':
        return 'scissors'

# List of valid options.
options = ['r', 'p', 's']

# Initialize score counters.
user_score = 0
computer_score = 0
ties = 0

# Game loop – play until user quits.
while True:
    # Ask user for their choice.
    user_choice = input("\nEnter r (rock), p (paper), s (scissors), or q to quit: ").lower()

    # Check if the user wants to quit.
    if user_choice == 'q':
        break  # Exit the game loop.

    # Check for valid input
    if user_choice not in options:
        print("Invalid input. Please enter r, p, s, or q.")
        continue  # Skip rest of loop and ask again.

    # Computer makes a random choice.
    computer_choice = random.choice(options)

    # Show both choices in full words
    print(f"\nYou chose {get_full_name(user_choice)}.")
    print(f"Computer chose {get_full_name(computer_choice)}.")

    # Determine the winner and update scores.
    if user_choice == computer_choice:
        print("It's a tie!")
        ties += 1
    elif (user_choice == 'r' and computer_choice == 's') or \
         (user_choice == 'p' and computer_choice == 'r') or \
         (user_choice == 's' and computer_choice == 'p'):
        print("You win this round!")
        user_score += 1
    else:
        print("Computer wins this round!")
        computer_score += 1

    # Display current scores.
    print(f"\nScoreboard:")
    print(f"You: {user_score}")
    print(f"Computer: {computer_score}")
    print(f"Ties: {ties}")

# Final message after quitting the game.
print("\nThanks for playing! Final scores:")
print(f"You: {user_score} | Computer: {computer_score} | Ties: {ties}")
