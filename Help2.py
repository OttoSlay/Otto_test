#
zeros = [[0] * 5 for i in range(5)]
print(zeros)
zeros[0][0] = 1
print(zeros)

#Создаёт словарь “страна → языки” и делает список стран, где языков больше одного.
countries = {
    "Россия": ['русский'],
    "Беларусь": ["белорусский", "русский"],
    "Бельгия": ["немецкий","французский","нидерландский"]
}
mult_lang = [country for (country, lang) in countries.items() if len(lang) > 1]
print(mult_lang)
countries = {country: capital for country, capital in [("rus", "mow"), ("bel", "minsk")]}
print(countries)
