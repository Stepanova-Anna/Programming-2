coun_cit = {
    "Россия": ["Москва", "Санкт-Петербург", "Калининград"],
    "Франция": ["Париж", "Лион", "Марсель", "Версаль"],
    "Великобритания": ["Лондон", "Манчестер", "Ливерпуль", "Глазго"],
    "Германия": ["Берлин", "Мюнхен", "Дрезден", "Кёльн"]
}


def find_country(city, coun_cit):
    for country, cities in coun_cit.items():
        if city in cities:
            return country
    return f"{city} не найден"


def avail_cities(coun_cit):
    cities = []
    for city_list in coun_cit.values():
        cities.extend(city_list)
    return cities


while True:

    available_cities = avail_cities(coun_cit)
    print("Список городов:", ", ".join(available_cities))

    city = input("Введите название города: ")
    country = find_country(city, coun_cit)
    print(f"Город {city} находится в стране {country}")
    print()

