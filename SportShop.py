contador1 = 0
contador2 = 0

while contador1 < 6:
    precio = int(input("Product price: "))

    if precio > 100000:
        contador2 += 1

    contador1 += 1

print("Products that cost more than 100000:", contador2)