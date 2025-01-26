def organizar(numeros):
    numeros_unicos = set(numeros)
    numeros_ordenados = sorted(numeros_unicos)
    return numeros_ordenados

numeros = [3, 7, 8, 18, 3, 0, 7]
lista_final = organizar(numeros)

print(f"Lista de regalos organizados: {lista_final}")

def organizeInventory(toys):
    inventory = {}

    for toy in toys:
        category = toy["category"]
        name = toy["name"]
        quantity = toy["quantity"]

        if category not in inventory:
            inventory[category] = {}

        if name in inventory[category]:
            inventory[category][name] += quantity
        else:
            inventory[category][name] = quantity

    return inventory

toys = [
    {"name": "Teddy Bear", "quantity": 5, "category": "Plushies"},
    {"name": "Lego Set", "quantity": 3, "category": "Building"},
    {"name": "Teddy Bear", "quantity": 2, "category": "Plushies"},
    {"name": "Drone", "quantity": 1, "category": "Electronics"},
    {"name": "Lego Set", "quantity": 4, "category": "Building"},
    {"name": "Puzzle", "quantity": 6, "category": "Brain Games"}
]

result = organizeInventory(toys)
print(result)