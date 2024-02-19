# -*- coding: utf-8 -*-
"""
Question 1:
"""

def square_root_generator(limit):
    n = 1
    while n <= limit:
        yield n ** 0.5
        n += 1

limit = 5
generator = square_root_generator(limit)

lista = []
for sqrt_value in generator:
    lista = lista.append(sqrt_value)

print(f"Sum: {sum(lista)}")

"""
Question 2:
"""

def square_root_generator(limit):
    n = 1
    while n <= limit:
        yield n ** 0.5
        n += 1

limit = 13
generator = square_root_generator(limit)

lista = []
for sqrt_value in generator:
    lista = lista.append(sqrt_value)

print(f"Sum: {sum(lista)}")

"""
Question 3:
"""

def people_1():
    for i in range(1, 6):
        yield {"ID": i, "Name": f"Person_{i}", "Age": 25 + i, "City": "City_A"}

for person in people_1():
    print(person)


def people_2():
    for i in range(3, 9):
        yield {"ID": i, "Name": f"Person_{i}", "Age": 30 + i, "City": "City_B", "Occupation": f"Job_{i}"}

total = 0

for person in people_1():
    total += person["Age"]

for person in people_2():
    total += person["Age"]

# Print the total age
print("Total:", total)

"""
Question 4
"""
merged = {}

for person in people_1():
    merged[person["ID"]] = person

for person in people_2():
    if person["ID"] in merged:
        merged[person["ID"]].update(person)
    else:
        merged[person["ID"]] = person

total = sum(person["Age"] for person in merged.values())

for person in merged.values():
    print(person)

print("Total", total)
