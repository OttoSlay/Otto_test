text = "Питон - это круто!"
def text_operation(text):
    print(text[:6])
    print(text[:-2])
    print(text[::-1])
    print(text[::2])
text_operation(text)
    
def even_index_elements(numbers):
    return numbers[::2]
print(even_index_elements([10,25,30,45,50,65,70]))

def shop_list(shopping):
    shopping[1] = ("батон")
    shopping.remove("сыр")
    shopping.append("йогурт")
    return shopping
print(shop_list(["молоко","хлеб","сыр","яблоки"]))

def list (a,b):
    merged = a + b 
    reversed_list = merged[::-1]
    print(reversed_list)
    print("Длинна списка: ", len(reversed_list))
list([1,3,5],[2,4,6])

def unique_elements(data):
    unique_data = []
    for x in data:
        if x not in unique_data:
            unique_data.append(x)
    return unique_data
print(unique_elements([1, 2, 2, 3, 4, 4, 5, 1]))

def update_countries(countries):
    countries["Германия"] = "Берлин"
    countries["Испания"] = "Барселона"
    for country, capital in countries.items():
        print(f"Столица{capital} находиься в стране {country}")
update_countries({
    "Россия": "Москва",
    "Италия": "Рим",
    "Испания": "Мадрид"
})


def analyze(word):
    letters = set(word)
    unique_count = len(letters)
    vowels = set("аеёиоуыэюя")
    vowels_in_word = letters & vowels
    print("Уникальных букв:",unique_count)
    print("Гласные в слове:", vowels_in_word)
analyze("Программирование")

def invert_dict(countries_and_capitals):
    return {capital: country for country, capital in countries_and_capitals.items()}
print(invert_dict({
    "Россия": "Москва",
    "Франция": "Париж",
    "Япония": "Токио"}))

def modify_movies(movies):
    movies.sort()
    movies.insert(0, "Интерстеллар")
    movies.pop()
    return movies
print(modify_movies(["Титаник", "Голый пистолет", "Аэроплан", "Мстители", "Смешарики в 3D"]))