cono = 3000
vaso = 4000
banana_split = 9000

total_vendido = 0
clientes = 0

cono_count = 0
vaso_count = 0
banana_count = 0

continuar = "yes"

while continuar == "yes":
    producto = input("Enter the product name you want to buy (cono / vaso / banana split): ").lower()
    if producto not in ["vaso", "cono", "banana split"]:
        print("Invalid product")
        continue
    cantidad = int(input(f"How many {producto} would you like?: "))
    if producto == "cono":
        precio = cono
        cono_count += cantidad
    elif producto == "vaso":
        precion = vaso
        vaso_count += cantidad
    elif producto == "banana split":
        precio = banana_split
        banana_count += cantidad

    total_cost = precio * cantidad

    print(f"Total for this client: {total_cost}.")

    total_vendido += total_cost
    clientes += 1

    continuar = input("Is there another client? (yes/no): ").lower()
if cono_count > vaso_count and cono_count > banana_count:
    mas_pedido = "cono"
elif vaso_count > cono_count and vaso_count > banana_count:
    mas_pedido = "vaso"
else:
    mas_pedido = "banana split"

print("\n___ Final Report ___")
print(f"Total sold: {total_vendido}")
print(f"Total Clients: {clientes}")
print(f"Most ordered product: {mas_pedido}")