def encryption(language, step, text):
    """Shift every letter of the text by step positions (Caesar cipher).

    language: 'ru' for the Russian alphabet, anything else for English
    step: shift size; negative values decrypt
    text: the string to process
    """
    # English alphabet by default: lowercase and uppercase
    sp1, sp2 = 'abcdefghijklmnopqrstuvwxyz', 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    result = ''
    # Switch to the Russian alphabet if requested (no 'ё' here)
    if language.lower() == 'ru':
        sp1, sp2 = 'абвгдежзийклмнопрстуфхцчшщъыьэюя', 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'

    for i in text:
        if i.isalpha():
            # Pick the alphabet that matches the letter's case
            sp = sp1
            if i.isupper(): sp = sp2
            # Find the letter's position, shift it, wrap around with %
            new_letter = (sp.index(i) + step) % len(sp)
            result += sp[new_letter]
        else:
            # Keep spaces, digits and punctuation unchanged
            result += i

    return result


# User input
chose = input('Зашифровать или Расшифровать текст? (з/р): ')  # encrypt or decrypt
lang = input('Language. ru/eng: ')
st = int(input('Step: '))
txt = input('Text: ')

# Decrypting is the same as encrypting with a negative step
if chose.lower() == 'з':
    print(encryption(lang, st, txt))
else:
    print(encryption(lang, -st, txt))