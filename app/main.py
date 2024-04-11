lucky_number = 777
pi = 3.14
one_is_a_prime_number = False
name = "Richard"
my_favourite_films = [
    "The Shawshank Redemption",
    "The Lord of the Rings: The Return of the King",
    "Pulp Fiction",
    "The Good, the Bad and the Ugly",
    "The Matrix",
]
profile_info = ("michel", "michel@gmail.com", "12345678")
marks = {
    "John": 4,
    "Sergio": 3,
}
collection_of_coins = {1, 2, 25}

sorted_variables = {"mutable": [], "immutable": []}

# Перевіряємо тип змінних і додаємо їх до відповідних списків
for variable in [lucky_number, pi, one_is_a_prime_number, name, my_favourite_films]:
    if isinstance(variable, (list, dict, set)):
        sorted_variables["mutable"].append(variable)
    else:
        sorted_variables["immutable"].append(variable)

# Додаємо кортеж profile_info до списку "immutable"
sorted_variables["immutable"].append(profile_info)

# Додаємо marks та collection_of_coins до списку "mutable"
sorted_variables["mutable"].extend([marks, collection_of_coins])
