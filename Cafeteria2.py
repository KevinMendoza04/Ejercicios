coffe = 4000
capuchino = 7000
pastel = 6000

condicional = "yes"

total_dia = 0

while condicional == "yes":

    compra = input("What would you like to purchase? (coffee / capuchino / pastel): ").lower()
    cantidad = int(input("How many would you like?: "))

    if compra == "coffee":
        total = coffe * cantidad

    elif compra == "capuchino":
        total = capuchino * cantidad

    elif compra == "pastel":
        total = pastel * cantidad

    else:
        print("Invalid product.")
        continue

    if total > 20000:
        descuento = total * 0.10
        total = total - descuento
        print("You received a 10% discount!")

    print(f"Total for this client: {total}")

    total_dia += total

    condicional = input("Would you like to register another client? (yes / no): ").lower()


print("\n--- End of the day report ---")
print(f"Total accumulated sales: {total_dia}")