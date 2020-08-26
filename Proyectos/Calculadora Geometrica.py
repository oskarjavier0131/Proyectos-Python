# Esta es calculadora Geometrica

menu = """ 
Bienvenido a la Calculadora Geometrica de JAVIER 😎😎😎

1 - Area y perimetro de un CUADRADO
2 - Area y perimetro de un RECTANGULO
3 - Area y perimetro de un TRIANGULO RECTANGULO

ELIGE UNA OPCIÒN: """

opcion = int(input(menu))
# AREA Y PERIMETRO DE UN CUADRADO
if opcion == 1:
    lado_a = input("Ingrese un lado del cuadrado: ")
    lado_a = int(lado_a)
    area = lado_a**2
    perimetro =  (4*lado_a)
    area = str(area)
    perimetro = str(perimetro)
    print(" El Area del cuadrado es" + " " + area + " " +"cm" + " " + "y su perimetro es" + " " + perimetro + " " +"cm")
# AREA Y PERIMETRO DE UN RECTANGULO    
elif opcion == 2:
    base = int(input("Ingrese la base del rectangulo: "))
    altura = int(input("Ingrese la altura del rectangulo: "))
    area= base * altura
    perimetro = (base * 2)+(altura*2)
    area = str(area)
    perimetro = str(perimetro)
    print("El area del rectangulo es" + " " + area + " " + "y su perimetro es" + " " + perimetro)
# AREA Y PERIMETRO DE UN TRIANGULO RECTANGULO    
elif opcion == 3:
    base = input("Ingrese la base del triangulo: ")
    base = int(base)
    altura = input("Ingrese la altura del triangulo: ")
    altura = int(altura)
    area = (base * altura)/2
    perimetro = (base*2) + (altura*2)
    area = str(area)
    perimetro = str(perimetro)
    print("El area del Triangulo Rectangulo  es" + " " + area + " " + "y su perimetro es" + " " + perimetro)
else:
    print("elige una opciòn valida por favor")