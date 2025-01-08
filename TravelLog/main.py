#Sözlük oluşturma
travel_log = [
    {
        "country": "France",
        "visits": 12,
        "cities": ["Paris", "Lille", "Dijon"]
    },
    {
        "country": "Germany",
        "visits": 5,
        "cities": ["Berlin", "Hamburg", "Stuttgart"]
    },
]

#Sözlüğe eklenecek bilgileri ayarlamak için fonksiyon oluşturma
def add_new_country(country_visited, times_visited, cities_visited):
    new_country = {}
    new_country["country"] = country_visited
    new_country["visits"] = times_visited
    new_country["cities"] = cities_visited
    travel_log.append(new_country)

#Oluşturulan işelvi çagırıp girdileri verme
add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])

#Sözlüğü kullanıcıya bildirme
print(travel_log)