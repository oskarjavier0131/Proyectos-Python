# CONVERSOR DE MONEDAS INTERNACIONALES

menu = """ 
Bienvenido al conversor de monedas de JAVIER 😎😎😎

1 - Pesos colombianos
2 - Pesos argentinod
3 - Pesos mexicanos

Elige una opciòn: """

opcion = int(input(menu))

if opcion == 1:
    pesos = float(input("¿Cuanto pesos colombianos tienes?: "))
    valor_dolar = 3875
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("Tienes $" + dolares + " " + "dolares") 
elif opcion == 2:
    pesos = float(input("¿Cuanto pesos argentinos tienes?: "))
    valor_dolar = 65
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("Tienes $" + dolares + " " + "dolares") 
elif opcion == 3:
    pesos = float(input("¿Cuanto pesos mexicanos tienes?: "))
    valor_dolar = 24
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("Tienes $" + dolares + " " + "dolares")
else:
    print("Ingresa una opciòn valida por favor")

    












