from random import choice
import time


# Prints empty lines to separate sections of the game.
def print_spacing():
    print()
    print()


# Display the game title and rules.
print('=' * 50)
print(' ' * 17 + 'FIELD OF WONDERS')
print('=' * 50)
print()

print('ПРАВИЛА ИГРЫ'.center(50))
print('-' * 50)
print('1. Играют трое, барабан крутят по очереди.')
print('2. Угадали букву: очки ваши, ход ваш.')
print('3. Промах или «банкрот»: ход переходит дальше.')
print('4. «Банкрот» обнуляет все ваши очки.')
print('5. Побеждает тот, у кого больше очков, а не')
print('   тот, кто отгадал слово.')
print('6. Буквы «Ё» в игре нет: везде используется «Е».')
print('=' * 50)
print_spacing()


# Store the words and their corresponding descriptions.
words = ['питон', 'арбуз', 'лампа', 'матрешка', 'телескоп',
         'вулкан', 'компас', 'самовар', 'клавиатура', 'пингвин']

descriptions = [
    'Змея и одновременно язык программирования',
    'Большая полосатая ягода, красная и сладкая внутри',
    'Предмет, который прогоняет темноту в комнате',
    'Деревянная кукла, внутри которой прячутся другие такие же',
    'Прибор, с помощью которого астрономы разглядывают звёзды',
    'Гора, которая иногда выбрасывает огонь и пепел',
    'Прибор со стрелкой, которая всегда показывает на север',
    'Русский прибор для кипячения воды, из него наливают чай',
    'Набор кнопок, на которых ты печатаешь текст',
    'Птица, которая не умеет летать и живёт в холодных краях'
]

# Store all possible wheel sectors: two rows of points and bankruptcy.
sectors = [
    100, 200, 300, 400, 500, 600, 700, 800, 900, 1000,
    150, 250, 350, 450, 550, 650, 750, 850, 950, 1050,
    'банкрот'
]

# Store player positions, names, and scores.
subs = ['first', 'second', 'third']
name_list = []
points_list = [0, 0, 0]

# Randomly select a word and find its corresponding description.
the_word = choice(words)
ind_the_word = words.index(the_word)
myst = descriptions[ind_the_word]

# Ask all three players to enter their names.
n = 0
while n != 3:
    name = input(f"enter {subs[n]} player's name: ").strip()
    if name:
        name_list.append(name)
        n += 1
    else:
        print('Invalid input')

print()

# Display the clue and hide the letters of the word.
print(f'Внимание, вопрос: {myst}')
s = []
s += '_' * len(the_word)
print(*s)
print_spacing()

# Initialize the current player and the turn-control variables.
ind = 0
flag = 0
sravni = ''

# Continue the game until the hidden word has been guessed.
while sravni != the_word:
    sravni = ''

    # Move to the next player after an unsuccessful turn.
    if flag == 1:
        ind += 1

    # Return to the first player after the third player.
    if ind == 3:
        ind = 0

    # Randomly select a wheel sector and wait for the player to spin.
    points = choice(sectors)
    spin = input(f'{name_list[ind]}, press Enter to spin the reel: ')

    while spin.strip():
        print('Invalid input')
        spin = input(f'{name_list[ind]}, press Enter to spin the reel: ')

    if points != 'банкрот':
        # Ask the player to enter a letter.
        char = input(f'{points} очков на барабане! Буква: ')

        # Validate the entered letter.
        while not char.strip() or len(char.strip()) != 1 or not char.strip().isalpha():
            if not char.isalpha() or len(char.strip()) != 1:
                print('Invalid input')
            char = input(f'{points} очков на барабане! Буква: ')

        char = char.strip().lower()

        if char in the_word:
            check = char
            check = check.strip().lower()

            # Do not allow the player to choose an already revealed letter.
            while check in s or check == '' or not check.isalpha() or len(check) != 1:
                if len(check) != 1 or not check.isalpha():
                    print('Invalid input')
                    check = input('Выберите другую букву: ')
                else:
                    check = input('Эта буква уже была, выберите другую: ')
                check = check.strip().lower()

            check = check.strip().lower()

            if check in the_word:
                # Award points and let the player keep the turn.
                flag = 0
                points_list[ind] += points
                print('Есть такая буква')

                # Reveal every occurrence of the guessed letter.
                for i in range(len(s)):
                    if the_word[i] == check:
                        s[i] = the_word[i]
                    print(s[i] + ' ', end='')
            else:
                # Pass the turn if the new letter is incorrect.
                flag = 1
                print('Нет такой буквы')
        else:
            # Pass the turn if the guessed letter is not in the word.
            flag = 1
            print('Нет такой буквы')

    elif points == 'банкрот':
        # Reset the player's score and pass the turn.
        flag = 1
        print(f'Сектор {points} на барабане!')
        print(f'К сожалению, {name_list[ind]}, вы теряете все свои очки')
        points_list[ind] = 0

    print('\n')

    # Build a string from the revealed letters to check if the word is complete.
    for f in s:
        sravni += f


# Display the end-of-game screen and reveal the hidden word.
print()
print('=' * 50)
print('ИГРА ОКОНЧЕНА'.center(50))
print('=' * 50)
print()
print(f'Загаданное слово: {the_word.upper()}'.center(50))
time.sleep(1)
print_spacing()

# Find the highest score and collect all players with that score.
top = max(points_list)
winners = []

for i in range(3):
    if points_list[i] == top:
        winners.append(name_list[i])

# Announce the winner or winners.
if len(winners) == 1:
    print('И ПОБЕДИТЕЛЬ ИГРЫ...'.center(50))
    time.sleep(1.5)
    print()
    print(f'*** {winners[0].upper()} ***'.center(50))
else:
    print('У НАС НИЧЬЯ! ПОБЕДИТЕЛИ:'.center(50))
    time.sleep(1.5)
    print()
    print(f'*** {", ".join(winners).upper()} ***'.center(50))

print(f'{top} очков'.center(50))
time.sleep(1)
print_spacing()

# Display the final scoreboard, sorted by score.
print('ИТОГОВАЯ ТАБЛИЦА'.center(50))
print('-' * 50)
results = sorted(zip(points_list, name_list), reverse=True)

for pts, name in results:
    print(f'{name:<30}{pts:>10} очков')

print('=' * 50)
print('Спасибо за игру!'.center(50))
print('=' * 50)