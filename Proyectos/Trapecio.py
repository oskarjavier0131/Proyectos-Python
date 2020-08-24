    ## AREA Y PERIMETRO DEL TRAPECIO
    
    base_2 = int(input("Ingrese la base superior del trapecio: "))

    altura = int(input("Ingrese la altura del trapecio: "))
    
    area = (base_1+base_2)*altura
    perimetro = (base_1 + base_2)+ (altura*2)
    area = str(area)
    perimetro = str(perimetro)
    print("El area del Trapecio es" + " " + area + " " + "y su perimetro es" + " " + perimetro)
