vainilla = 0
chocolate = 0
strawberry = 0

for i in range(1, 6, 1):
    helado = input(f"Write ice cream flavor #{i}: ").strip().lower()

    if helado == "vainilla":
        vainilla += 1
    elif helado == "chocolate":
        chocolate += 1
    elif helado == "strawberry":
        strawberry += 1

print("Vanilla Ice creams:", vainilla)
print("Chocolate Ice creams:", chocolate)
print("Strawberry Ice creams:", strawberry)