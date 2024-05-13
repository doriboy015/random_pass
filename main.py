import random

def generate_password(length, chars):
    fin_pass = ''
    for i in range(int(length)):
        fin_pass += random.choice(chars)
    return fin_pass

digits = '23456789'
lowercase_letters = 'abcdefghjkmnpqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKMNPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_.'
exc = 'il1Lo0O'

chars = ''    #словарь для генерации пароля

cntPw = input('Укажите количество паролей для генерации: ')
lenPw = input('Укажите длину одного пароля: ')
dig_on = input('Включать ли цифры 0123456789? (y/n) ')
ABC_on = input('Включать ли прописные буквы ABCDEFGHIJKLMNOPQRSTUVWXYZ? (y/n) ')
abc_on = input('Включать ли строчные буквы abcdefghijklmnopqrstuvwxyz? (y/n) ')
ch_on = input('Включать ли символы !#$%&*+-=?@^_? (y/n) ')
exc_on = input('Исключать ли неоднозначные символы il1Lo0O? (y/n) ')

if dig_on == 'y':
    for i in range(len(digits)):
        chars += digits[i]
if ABC_on == 'y':
    for i in range(len(uppercase_letters)):
        chars += uppercase_letters[i]
if abc_on == 'y':
    for i in range(len(lowercase_letters)):
        chars += lowercase_letters[i]
if ch_on == 'y':
    for i in range(len(punctuation)):
        chars += punctuation[i]
if exc_on == 'y':
    for i in range(len(exc)):
        chars += exc[i]

for i in range(int(cntPw)):
    print(generate_password(lenPw, chars))

