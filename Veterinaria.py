Dog = "Protein"
Cat = "Tuna"
Rabbit = "Carrot"
ingreso = input("¿What type of pet do you have?: ").lower()
if ingreso == "dog":
        print(f"The best food for your dog is: {Dog}.")
elif ingreso == "cat":
        print(f"The best food for your cat is: {Cat}.")
elif ingreso == "rabbit":
        print(f"The best food for your rabbit is: {Rabbit}.")
else:
    print("Invalid input.")