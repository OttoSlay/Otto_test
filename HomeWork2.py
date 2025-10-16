#Дз от 14 Октября

#1 Часть 
text=input("Введите фразу: ")
if "Привет" in text:
    print("И тебе привет!")
elif "Пока" in text:
    print("Уже уходишь? :c")
else:
    print("Ты молчалив сегодня...")

#2 Часть
n=int(input("Введите число n: "))
for i in range (1, n+1):
    print(f"{i}^2 = {i**2}, {i}^3 = {i**3}")

#3 Часть 
secret=7 
while True:
    guess=int(input("Угадай число: "))
    if guess < secret:
        print("Мало!")
    elif guess > secret:
        print("Много!")
    else:
        print("Верно!")
        break 

#4 Часть
text=input("Введите слово: ")
vowels="аеёиоуыэюя"
for index, letter in enumerate(text):
    if letter.lower() in vowels:
        print(index, letter)

#5 Часть
for frog in range(1,4):
    for pad in range(1,4):
        if frog == pad:
            continue
        print(f"Лягушка {frog} прыгает на кочку {pad}")

