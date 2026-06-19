# Этот код генерирует пароль И затем проверяет его на сложность

import random

print("Введите слово")

word = input()

while word.isalpha() == False:
    print(
        "Предложение должно состоять только из букв и содержать в себе одно слово, введите еще раз"
    )
    word = input()

chrs = []
passwd = []
symbols = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "=", "+"]

for i in word:
    chrs.append(i.lower())
random.shuffle(chrs)

for _ in range(random.randrange(1, 10)):
    passwd += str(random.randint(0, 9))

for _ in range(random.randrange(1, 10)):
    passwd += random.choice(symbols)

for j in range(random.randrange(0, len(chrs))):
    chrs[j] = chrs[j].upper()

passwd += chrs
random.shuffle(passwd)

passwd_str = "".join(passwd)

with open("passwd.txt", "a", encoding="utf-8") as file:
    file.write(f"""Слово: {word}
Пароль: {passwd_str}

""")

print()
print("Ваш пароль:")
print(passwd_str)
print("Пароль сохранен в файл passwd.txt")
