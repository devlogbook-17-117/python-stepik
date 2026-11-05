from random import choice


def get_all_access_symbols():
    """Ask the user which character groups to use and return the allowed characters."""
    # Character groups, in the same order as the first four questions below
    access_letters_list = ["0123456789", "ABCDEFGHIJKLMNOPQRSTUVWXYZ", "abcdefghijklmnopqrstuvwxyz",
                           "!#$%&*+-=?@^_"]
    print()
    print('*' * 5, '(yes - y, no - n)', '*' * 5)
    # Questions for the user; the last one is about ambiguous characters
    asks_list = ['U need digits "0123456789"? ', 'U need "ABCDEFGHIJKLMNOPQRSTUVWXYZ"? ',
                 'U need "abcdefghijklmnopqrstuvwxyz"? ', 'U need symbols "!#$%&*+-=?@^_"? ',
                 'Use ambiguous letters "il1LIo0O"? ']
    access_letters = ''
    # Ask the first four questions (all except the last one) and
    # add the matching character group when the answer is 'y'
    for i in range(len(asks_list) - 1):
        ask = input(asks_list[i]).lower()
        if ask == 'y':
            access_letters += access_letters_list[i]

    # The last question: if the user doesn't want ambiguous characters, remove them
    if input(asks_list[len(asks_list) - 1]).lower() != 'y':
        access_letters = del_elements(access_letters)

    return access_letters


def del_elements(letters):
    """Remove visually ambiguous characters from the given string and return a list."""
    wrong_letters = 'il1LIo0O'
    letters = list(letters)  # Convert to a list so items can be removed
    for char in wrong_letters:
        # Remove every occurrence of the current ambiguous character
        while char in letters:
            letters.remove(char)
    return letters


def generate_password(kol_vo, length, access_letters):
    """Generate `kol_vo` numbered passwords of the given length from the allowed characters."""
    password_list = list()
    for i in range(kol_vo):
        password = ''
        # Build the password by picking a random character `length` times
        for _ in range(length):
            password += choice(access_letters)
        # Add a sequence number before the password (1., 2., 3., ...)
        password_list.append(str(i + 1) + '. ' + password)
    return password_list


# --- Main program ---
# Get the number of passwords and their length from the user
ask_kol_vo_passw = int(input('How many passwords u want: '))
ask_length_passw = int(input('Password length: '))
# Ask which characters are allowed
chars = get_all_access_symbols()

# Generate the passwords
result = generate_password(ask_kol_vo_passw, ask_length_passw, chars)

# Print the passwords, one per line
print()
print('Your passwords:')
print(*result, sep='\n')