import random

def coin_toss():
    # Randomly select "Heads" or "Tails"
    result = random.choice(["Heads", "Tails"])
    return result

def main():
    print("Welcome to the Coin Toss Game!")
    print("Guess the outcome of the coin toss: Heads or Tails")

    # Get the user's guess
    user_guess = input("Enter your guess (Heads/Tails): ").capitalize()
    
    # Check for valid input
    if user_guess not in ["Heads", "Tails"]:
        print("Invalid input. Please enter 'Heads' or 'Tails'.")
        return
    
    # Perform the coin toss
    result = coin_toss()
    
    # Display the result
    print(f"The coin toss result is: {result}")
    
    # Check if the user's guess matches the result
    if user_guess == result:
        print("Congratulations! You guessed correctly.")
    else:
        print("Sorry, better luck next time.")

# Run the game
main()
