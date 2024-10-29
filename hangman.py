import random


words = ["vicky", "khan", "codealpha", "programming", "computer"]
chosen_word = random.choice(words)
guessed_word = ["_"] * len(chosen_word)
incorrect_guesses = 0
max_incorrect_guesses = 6
guessed_letters = set()
print("Welcome to Hangman! Try to guess the word.")
while incorrect_guesses < max_incorrect_guesses and "_" in guessed_word:
    print("\nCurrent word:", " ".join(guessed_word))
    print(f"Incorrect guesses left: {max_incorrect_guesses - incorrect_guesses}")
    guess = input("Guess a letter: ").lower()
    
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single alphabetic character.")
        continue
    
    if guess in guessed_letters:
        print("You already guessed that letter. Try again.")
        continue
    
    
    guessed_letters.add(guess)
    
    if guess in chosen_word:
        
        for i, letter in enumerate(chosen_word):
            if letter == guess:
                guessed_word[i] = guess
        print("Good guess!")
    else:
        incorrect_guesses += 1
        print("Incorrect guess.")
    
if "_" not in guessed_word:
    print("\nCongratulations! You guessed the word:", chosen_word)
else:
    print("\nOut of guesses! The word was:", chosen_word)