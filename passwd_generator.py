# Этот код генерирует пароль И затем проверяет его на сложность

import random
import os
from datetime import datetime


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


clear_screen()
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

print(f"""
Куда вы хотите сохранить пароль?
      1. В файл passwd.txt (по умолчанию)
      2. Указать свое имя для файла

Выберите вариант ответа (введите 1 или 2)""")

while True:
    var_answ = input()
    try:
        var_answ = int(var_answ)
        if var_answ in [1, 2]:
            if var_answ == 1:
                name_file = "passwd.txt"
            else:
                print("Введите название файла")
                name_file = input()

                if not name_file.endswith(".txt"):
                    name_file += ".txt"
            break
        else:
            print("Введите либо 1 либо 2")
    except ValueError:
        print("Введите либо 1 либо 2")

current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

with open(name_file, "a", encoding="utf-8") as file:
    file.write(f"Время: {current_time}\nСлово: {word}\nПароль: {passwd_str}\n\n")
print(f"Пароль успешно сохранен в {name_file}")
print(f"Ваш пароль: {passwd_str}")

print(f"Показать все сохраненные пароли? (да/нет)")

while True:
    var_answ_2 = input().lower()
    try:
        if var_answ_2 == "да" or var_answ_2 == "нет":
            if var_answ_2 == "да":
                clear_screen()
                with open(name_file, "r", encoding="utf-8") as file:
                    file_read = file.read()
                    print(file_read)
            else:
                break
            break
        else:
            print("Введите либо да либо нет")
    except ValueError:
        print("Введите либо да либо нет")
