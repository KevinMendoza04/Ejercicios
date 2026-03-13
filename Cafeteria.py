café = 4000
té = 3500
jugo = 5000
ingreso = input("¿Que bebida desea?: ").lower()
cu = int(input(f"¿Cuantos {ingreso} deseas?: "))
if ingreso == "cafe":
    total = café * cu
elif ingreso == "te":
    total = té * cu
elif ingreso == "jugo":
    total = jugo * cu
else:
    print("Bebida no disponible")
    total = 0
print("Total: ", total)