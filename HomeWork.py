#1 Часть
name=input("Введите ваше имя: ")
print(f"Hola,{name}!Bienvenido!")

quite=input("Введите вашу любимую цитату: ")
author=input("Введитк второа цитаты: ")
print(f'"{author}"-{author}')

word=input("Введите слово: ")
count=int(input("Сколько раз повторить?"))
print(word * count )

phrase=input("Введите фразу: ")
print(phrase.upper())
print(phrase.lower())

#2 Часть
width=float(input("Введите ширину (в см): "))
height=float(input("Введите высоту (в см): "))
area=width * height
print(f"Площадь прямоугольника: {area} кв.см.")

age_years=int(input("Введите ваш возраст в годах: "))
age_months=age_years * 12
print(f"Ваш возраст состовляет примерно {age_months} месяцев.")

#3 Часть 
age=int(input("Введите ваш возраст: "))
name=input("Введите ваше имя: ")
if age >= 18 and name != "Иван":
    print("Доступ разрешен!")
else:
    print("Доступ запрещен!")