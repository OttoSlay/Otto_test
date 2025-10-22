text="Питон - это круто!"
print(text[:6])
print(text[:-2])
print(text[::-1])
print(text[::2])

numbers=[10,25,30,45,50,65,70]
even_index_numbers = numbers[::2]
print(even_index_numbers)

shopping=["молоко","хлеб","сыр","яблоки"]
shopping[1]="батон"
shopping.remove("сыр")
shopping.append("йогурт")
print(shopping)

a=[1,3,5]
b=[2,4,6]
mergen=a+b
reversed_list=mergen[::-1]
length=len(reversed_list)
print(reversed_list)
print("Длина списка:",length)

data = [1, 2, 2, 3, 4, 4, 5, 1]
unique_data= []
for x in data:
    if x not in unique_data:
        unique_data.append(x)
print(unique_data)

countries={
    "Россия": "Москва",
    "Италия": "Рим",
    "Испания": "Мадрид"}
countries["Германия"]="Берлин"
countries["Испания"]= "Барселона"
for country, capital in countries.items():
    print(f"Столица{capital} находится в стране {country}")

word="прокраммирование"
letters=set(word)
unique_count=len(letters)
vowels=set("аеёиоуыэюя")
vowels_in_word=letters & vowels
print("уникальных букв:", unique_count)
print("Гласные в слове:", vowels_in_word)

countries_and_capitals={
    "Россия": "Москва",
    "Франция": "Париж",
    "Япония": "Токио"}
countries_and_capitals = {capital: country for country, capital in countries_and_capitals.items()}
print(countries_and_capitals)

movies=["Титаник","Голый пистолет","Аэроплан","Мстители","Смешарики в 3D"]
movies.sort()
movies.insert(0,"Интерстеллар")
movies.pop()
print(movies)

nums=[15,2,30,4,50,6,75,8]
minimum=min(nums)
maximum=max(nums)
avarage=len(nums)
print("Минимум:", minimum)
print("Максимум:", maximum)
print("Среднее врифмитическое:", avarage)
nums_filtered=[x for x in nums if x <= avarage]
nums_filtered.sort()
print("Итоговый список:", nums_filtered)