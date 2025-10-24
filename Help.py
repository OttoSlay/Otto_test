#Подсказки 

a = 10
b = 3

print(a + b)  # сложение → 13
print(a - b)  # вычитание → 7
print(a * b)  # умножение → 30
print(a / b)  # деление → 3.333...
print(a // b) # целое деление → 3
print(a % b)  # остаток от деления → 1
print(a ** b) # возведение в степень → 1000

if условие:
    # код, если условие истинно
else:
    # код, если условие ложно

age = 18
if age >= 18:
    print("Ты совершеннолетний!")
else:
    print("Ты ещё маленький :)")


temperature = 15

if temperature > 25:
    print("Жарко ☀️")
elif temperature > 10:
    print("Тепло 🌤️")
else:
    print("Холодно 🥶")

age = 20
city = "Москва"

if age >= 18 and city == "Москва":
    print("Доступ разрешён!")
else:
    print("Доступ запрещён!")

#Списки и циклы (for, while)
fruits = ["яблоко", "банан", "вишня"]
print(fruits)
print(fruits[0])  # яблоко
print(fruits[1])  # банан
print(fruits[-1]) # вишня (последний)

fruits.append("груша")    # добавить в конец
fruits.remove("банан")    # удалить по значению
print(fruits)

#Цикл for Позволяет повторять действия для каждого элемента списка:
for fruit in fruits:
    print("Я люблю", fruit)
Я люблю яблоко
Я люблю вишня
Я люблю груша

#Цикл while Повторяет действия, пока условие истинно:
i = 1
while i <= 5:
    print("Счёт:", i)
    i += 1
Счёт: 1
Счёт: 2
Счёт: 3
Счёт: 4
Счёт: 5

#Перебор с индексом (enumerate)
for i, fruit in enumerate(fruits, start=1):
    print(f"{i}. {fruit}")
1. яблоко
2. вишня
3. груша

def имя_функции(аргументы):
    # тело функции
    return результат
