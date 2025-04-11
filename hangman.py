import random

# List of words to choose from
word_list = ['python', 'programming', 'hangman', 'developer', 'computer', 'software', 'algorithm']

# Function to display the current state of the word and guesses
def display_word(word, guessed_letters):
    displayed_word = ''.join([letter if letter in guessed_letters else '_' for letter in word])
    return displayed_word

# Main game function
def play_hangman():
    # Select a random word from the list
    word = random.choice(word_list)
    guessed_letters = []
    incorrect_guesses = 0
    max_incorrect_guesses = 6  # Set the limit of incorrect guesses
    
    print("Welcome to Hangman!")
    print(f"Guess the word. You have {max_incorrect_guesses} incorrect guesses allowed.")
    
    # Game loop
    while incorrect_guesses < max_incorrect_guesses:
        # Display the current state of the word
        print(f"Word: {display_word(word, guessed_letters)}")
        print(f"Incorrect guesses left: {max_incorrect_guesses - incorrect_guesses}")
        
        # Get the player's guess
        guess = input("Guess a letter: ").lower()
        
        # Validate the input
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a valid single letter.")
            continue
        
        # Check if the letter has already been guessed
        if guess in guessed_letters:
            print("You already guessed that letter. Try again.")
            continue
        
        # Add the guess to the guessed letters
        guessed_letters.append(guess)
        
        # Check if the guess is in the word
        if guess in word:
            print(f"Good guess! The letter '{guess}' is in the word.")
        else:
            incorrect_guesses += 1
            print(f"Oops! The letter '{guess}' is not in the word.")
        
        # Check if the player has guessed the word
        if all(letter in guessed_letters for letter in word):
            print(f"Congratulations! You guessed the word: {word}")
            break
    
    # If the player runs out of incorrect guesses
    if incorrect_guesses == max_incorrect_guesses:
        print(f"Game over! The word was: {word}")

# Run the game
if __name__ == "__main__":
    play_hangman()