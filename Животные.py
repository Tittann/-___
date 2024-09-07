import os

# Создание файла "Домашние животные"
with open("Домашние_животные", "w") as f:
    f.write("Собаки\n")
    f.write("Кошки\n")
    f.write("Хомяки\n")

# Создание файла "Вьючные животные"
with open("Вьючные_животные", "w") as f:
    f.write("Лошади\n")
    f.write("Верблюды\n")
    f.write("Ослы\n")

# Объединение файлов
with open("Друзья_человека", "w") as f:
    with open("Домашние_животные", "r") as f1:
        f.write(f1.read())
    with open("Вьючные_животные", "r") as f2:
        f.write(f2.read())

# Просмотр содержимого файла
with open("Друзья_человека", "r") as f:
    print(f.read())

# Переименование файла
os.rename("Друзья_человека", "Друзья_человека.txt")