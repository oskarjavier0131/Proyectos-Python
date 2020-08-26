# CONVERSOR DE MONEDAS INTERNACIONALES

def conversor(tipo_pesos, valor_dolar):
    pesos = float(input(" ¿Cuanto pesos " + tipo_pesos +  " tienes?: "))
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("Tienes $" + dolares + " " + "dolares")

menu = """ 
Bienvenido al conversor de monedas de JAVIER 😎😎😎

1 - Pesos colombianos
2 - Pesos argentinod
3 - Pesos mexicanos

Elige una opciòn: """

opcion = int(input(menu))

if opcion == 1:
    conversor("colombianos", 3875)
elif opcion == 2:
    conversor("argentinos", 65)   
elif opcion == 3:
    conversor("mexicanos", 24)
else:
    print("Ingresa una opciòn valida por favor")

    












