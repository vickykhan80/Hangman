 # Hangman Game
This is a simple Python implementation of the classic Hangman game. The program selects a random word from a predefined list, and the player has to guess it letter by letter. The game ends when the player either guesses the word or reaches the maximum number of incorrect guesses
## Features
+ Random word selection from a predefined list.
+ Tracks guessed letters and prevents duplicate guesses.
+ Limits incorrect guesses, ending the game if the limit is reached.
+ Simple and interactive command-line interface.
##  Requirements
_pkg install python_
## Termux Setup Instructions

   _pkg update && pkg upgrade_

   _pkg install python_

   _git clone https://github.com/vickykhan80/Hangman.git_
   
   _cd hangman-game_

   _python hangman.py_

   ## How to Play
1.The game will select a random word from the list.
2.You have 6 attempts to guess the word correctly by guessing one letter at a time.
3. For each guess:
+ If correct, the letter will be revealed in the word.
+ If incorrect, you lose one attempt.
4. If you guess the word before running out of attempts, you win. Otherwise, the game reveals the word at the end.

## License
This project is open source and available under the MIT License
## author
*Vicky Khan*
