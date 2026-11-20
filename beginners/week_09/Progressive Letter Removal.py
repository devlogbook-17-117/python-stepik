# Read the text and append the ending phrase
text = input() + ' запретил букву'


def get_unique_letters(word):
    """Return a string of unique letters from the word, ignoring spaces."""
    unique_letters = ''
    for i in word:
        # Add the character only if it is new and is not a space
        if i not in unique_letters and i != ' ':
            unique_letters += i
    return unique_letters


# Letters are banned in alphabetical order
chars = sorted(get_unique_letters(text))
for j in chars:
    # Print the current text and the letter that is banned now
    print(text, j)
    # Remove the banned letter from the text
    text = text.replace(j, '')
    # Collapse extra spaces left after the removal
    text = ' '.join(text.split())