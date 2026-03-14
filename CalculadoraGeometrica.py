variable_yes = "si"
while variable_yes == "si":
    print(f"___BIENVENIDO A TU CALCULADORA___")
    ingreso = input("¿Quieres calular una figura 2D o 3D? (2d / 3d): ").lower().strip()
    try:
        if ingreso == "2d":
            while True:
                print("\nFiguras 2D")
                print(f"1. triangulo")
                print(f"2. circulo")
                print(f"3. cuadrado")
                print(f"4. rectangulo")
                print(f"5. triangulo rectangulo")
                print(f"0. volver al menú anterior")
                pregunta2d = input("Elige el número de figura: ").strip().replace("," , ".")
                if pregunta2d == "0":
                    break
                if pregunta2d == "1":
                    ingreso2d = (input("¿Elije una opcion de medicion: 1. Area / 2. Perímetro / 0. Volver?: ")).strip().replace("," , ".")
                    if ingreso2d == "0":
                        continue
                    elif ingreso2d == "1":
                        base = float(input("¿Cual es la base de tu triangulo?: ").strip().replace("," , "."))
                        altura = float(input("¿Cual es la altura de tu triangulo?: ").strip().replace("," , "."))
                        area1 = (base * altura) / 2
                        print(f"El area del triangulo es: {area1}")
                    elif ingreso2d == "2":
                        lado1 = float(input("¿Cuanto mide el lado 1?: ").strip().replace("," , "."))
                        lado2 = float(input("¿Cuanto mide el lado 2?: ").strip().replace("," , "."))
                        lado3 = float(input("¿Cuanto mide el lado 3?: ").strip().replace("," , "."))
                        Perimetro1 = lado1 + lado2 + lado3
                        print(f"El perímetro de tu triangulo es: {Perimetro1}")
                if pregunta2d == "2":
                    ingreso2d = (input("¿Elije una opcion de medicion: 1. Area / 2. Perímetro / 3. Diametro / 0. Volver?: ")).strip().replace("," , ".")
                    if ingreso2d == "0":
                        continue
                    radio = float(input("¿Cual es el radio de tu circulo?: ").strip().replace("," , "."))
                    if ingreso2d == "1":
                        area2 = 3.1416 * radio ** 2
                        print(f"El area del circulo es: {area2}")
                    elif ingreso2d == "2": 
                        perimetro2 = 2 * 3.1416 * radio
                        print(f"El perimetro del circulo es: {perimetro2}")
                    elif ingreso2d == "3":
                        diametro = 2 * radio
                        print(f"El perimetro del circulo es: {diametro}")
                if pregunta2d == "3":
                    ingreso2d = (input("¿Elije una opcion de medicion: 1. Area / 2. Perímetro / 3. Diagonal / 0. Volver?: ")).strip().replace("," , ".")
                    if ingreso2d == "0":
                        continue
                    lados = float(input("Cuanto miden los lados de tu cuadrado?: ").strip().replace("," , "."))
                    if ingreso2d == "1":
                        area = lados ** 2
                        print(f"El area del cuadrado es: {area}")
                    elif ingreso2d == "2": 
                        perimetro3 = 4 * lados
                        print(f"El perimetro del cuadrado es: {perimetro3}")
                    elif ingreso2d == "3":
                        diagonal = lados * (2 ** 0.5)
                        print(f"El perimetro del cuadrado es: {diagonal}")
                if pregunta2d == "4":
                    ingreso2d = (input("¿Elije una opcion de medicion: 1. Area / 2. Perímetro / 3. Diagonal / 0. Volver?: ")).strip().replace("," , ".")
                    if ingreso2d == "0":
                        continue
                    base = float(input("Cual es la base de tu rectangulo?: ").strip().replace("," , "."))
                    altura = float(input("Cual es la altura de tu rectangulo?: ").strip().replace("," , "."))
                    if ingreso2d == "1":
                        area3 = base * altura
                        print(f"El area del rectangulo es: {area3}")
                    elif ingreso2d == "2": 
                        perimetro4 = 2 * (base + altura)
                        print(f"El perimetro del rectangulo es: {perimetro4}")
                    elif ingreso2d == "3":
                        diagonal = (base ** 2 + altura ** 2) ** 0.5
                        print(f"El perimetro del rectabgulo es: {diagonal}")
                if pregunta2d == "5":
                    ingreso2d = (input("¿Elije una opcion de medicion: 1. Area / 2. Hipotenusa / 3. Perímetro / 0. Volver?: ")).strip().replace("," , ".")
                    if ingreso2d == "0":
                        continue
                    base = float(input("Cual es la base de tu Triangulo Rectangulo?: ").strip().replace("," , "."))
                    altura = float(input("Cual es la altura de tu Triangulo Rectangulo?: ").strip().replace("," , "."))
                    if ingreso2d == "1":
                        area = (base * altura) / 2
                        print(f"El area del Triangulo Rectangulo es: {area}")
                    elif ingreso2d == "2": 
                        hipotenusa = (base ** 2 + altura ** 2) ** 0.5
                        print(f"El perimetro del Triangulo Rectangulo es: {hipotenusa}")
                    elif ingreso2d == "3":
                        hipotenusa = (base ** 2 + altura ** 2) ** 0.5
                        perimetro5 = base + altura + hipotenusa
                        print(f"El perimetro del Triangulo Rectangulo es: {perimetro5}")                   
        elif ingreso == "3d":
            while True:    
                print("\nFIGURAS 3D")
                print(f"6. esfera")
                print(f"7. cubo")
                print(f"8. cilindro")
                print(f"9. cono")
                print(f"0. volver al menú anterior.")
                pregunta3d = input("Elige el número de figura: ").strip().replace("," , ".")
                if pregunta3d == "0":    
                    break
                if pregunta3d == "6":
                    operacion = input("¿Que deseas calcular? 1. Volumen / 2. Area superficial / 0. Volver?: ").strip().replace("," , ".")
                    if operacion == "0":
                        continue
                    radio = float(input("Ingresa el radio de la esfera: ").strip().replace("," , "."))
                    if operacion == "1":
                        volumen = (4/3) * 3.1416 * radio ** 3
                        print(f"El volumen de la esfera es: {volumen}")
                    elif operacion == "2":
                        area_superficial = 4 * 3.1416 * radio ** 2
                        print(f"El area superficial de la esfera es: {area_superficial}")
                if pregunta3d == "7":
                    operacion = input("¿Que deseas calcular? 1. Volumen / 2. Area superficial / 0. Volver?: ").strip().replace("," , ".")
                    if operacion == "0":
                        continue
                    lado = float(input("Ingresa el lado del cubo: ").strip().replace("," , "."))
                    if operacion == "1":
                        volumen = lado ** 3
                        print(f"El volumen del cubo es: {volumen}")
                    elif operacion == "2":
                        area = 6 * lado ** 2
                        print(f"El area superficial del cubo es: {area}")        
                if pregunta3d == "8":
                    operacion = input("¿Que deseas calcular? 1. Volumen / 2. Area superficial / 0. Volver?: ").strip().replace("," , ".")
                    if operacion == "0":
                        continue
                    radio = float(input("Ingresa el radio del cilindro: ").strip().replace("," , "."))
                    altura = float(input("Ingresa la altura del cilindro: ").strip().replace("," , "."))
                    if operacion == "1":
                        volumen = 3.1416 * radio ** 2 * altura
                        print(f"El volumen del cilindro es: {volumen}")
                    elif operacion == "2":
                        area = 2 * 3.1416 * radio * (altura + radio)
                        print(f"El area superficial del cilindro es: {area}")
                if pregunta3d == "9":
                    operacion = input("¿Que deseas calcular? 1. Volumen / 2. Area superficial / 0. Volver?: ").strip().replace("," , ".")
                    if operacion == "0":
                        continue
                    radio = float(input("Ingresa el radio del cono: ").strip().replace("," , "."))
                    altura = float(input("Ingresa la altura del cono: ").strip().replace("," , "."))
                    generatriz = (radio ** 2 + altura ** 2) ** 0.5
                    if operacion == "1":
                        volumen = (1/3) * 3.1416 * radio ** 2 * altura
                        print(f"El volumen del cono es: {volumen}")
                    elif operacion == "2":
                        area = 3.1416 * radio * (radio + generatriz)
                        print(f"El area superficial del cono es: {area}")     
        variable_yes = input("Quieres volver al início? (si/no): ").lower().strip()        
    except ValueError:
        print("Ingreso invalido, intenta de nuevo.")