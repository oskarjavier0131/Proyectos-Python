# IVA LATINO AMERICANO

def impuesto(pais, iva):
    valor_compra = int(input("Ingrese el valor neto su compra: "))
    compra_iva = (valor_compra*iva)
    compra_iva = round(compra_iva, 0)
    compra_iva = str(compra_iva)
    print(" El impuesto aplicado para tu compra en " + pais + " es de $ " + compra_iva)

menu = """
BIENVENIDO AL EVALUADOR DE CARGA TRIBUTARIA PARA LATINO AMERICA  DE JAVIER 😎😎😎
¿TU COMPRA FUE REALIZADA EN?

1 - URUGUAY
2 - ARGENTINA
3 - CHILE
4 - PERU
5 - BRAZIL
6 - MEXICO
7 - COLOMBIA
8 - HONDURAS
9 - ECUADOR
10 - PANAMA

ELIGE UNA OPCIÒN: """            

opcion = int(input(menu))

if opcion == 1:
    impuesto("Uruguay", 0.22)
elif opcion == 2:
    impuesto("Argentina", 0.21)
elif opcion == 3:
    impuesto("Chile", 0.19)    
elif opcion == 4:
    impuesto("Peru", 0.18)
elif opcion == 5:
    impuesto("Brazil", 0.17)
elif opcion == 6:
    impuesto("Mexico", 0.16)
elif opcion == 7:
    impuesto("Colombia", 0.19)                
elif opcion == 8:
    impuesto("honduras", 0.15)    
elif opcion == 9:
    impuesto("Ecuador", 0.12)    
elif opcion == 10:
    impuesto("Panamà", 0.7)    
else:
    print("Ingrese una opciòn valida")     

    





