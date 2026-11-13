from random import choice

# Gallows pictures: index = number of attempts left.
# Index 6 is the empty gallows, index 0 is the full hanged man.
gallows_and_body_parts = [
    r"""
+---+
|   |
|   O
|  /|\
|  / \
|
=========""",
    r"""
+---+
|   |
|   O
|  /|\
|  /
|
=========""",
    r"""
+---+
|   |
|   O
|  /|\
|
|
=========""",
    r"""
+---+
|   |
|   O
|  /|
|
|
=========""",
    r"""
+---+
|   |
|   O
|   |
|
|
=========""",
    r"""
+---+
|   |
|   O
|
|
|
=========""",
    r"""
+---+
|   |
|
|
|
|
=========""",
]

# Words to guess
words = [
    "осьминог", "муравей", "туманность", "помпеи", "герасим",
    "онегин", "байкал", "хамелеон", "сердце", "пульсар",
]

word = choice(words)             # secret word chosen randomly
guessed = ['_'] * len(word)      # current state of the word, e.g. ['_', 'а', '_']
letters = ''                     # all letters the player has already tried
attempts = 6                     # wrong guesses left


def get_letter():
    """Ask the player for a letter until the input is valid."""
    while True:
        letter = input('Enter a letter: ').lower()
        # Must be exactly one alphabetic character
        if len(letter) != 1 or not letter.isalpha():
            print("Invalid input, try again.")
        # Latin letters are not allowed, the words are in Russian
        elif letter.isascii():
            print("Please switch your keyboard layout to Russian.")
        # Don't accept the same letter twice
        elif letter in letters:
            print("This letter was already used.")
        else:
            return letter


print('*' * 17, 'HANGMAN', '*' * 17)
print(gallows_and_body_parts[attempts])  # show the empty gallows at the start


def play():
    """Play one round: ask for a letter and update the game state."""
    global attempts, letters
    print()
    print(*guessed)
    letter = get_letter()
    letters += letter  # remember the letter as used
    if letter in word:
        print("Correct!")
        # Open every position where the letter occurs
        for i in range(len(word)):
            if word[i] == letter:
                guessed[i] = letter
        print(*guessed)
    else:
        # Wrong letter: lose an attempt and draw the next stage
        attempts -= 1
        print(letter.upper(), 'is', 'Wrong letter')
        print(gallows_and_body_parts[attempts])


# Main loop: continue while there are attempts left and the word is not fully guessed
while attempts != 0 and guessed != list(word):
    play()

# Game result
print()
if guessed != list(word):
    print("You lost!")
    print("The word was:", word)
else:
    print("You won!")
    print("The word is:", word)