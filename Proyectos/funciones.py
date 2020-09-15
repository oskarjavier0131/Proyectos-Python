# def imprimir_mensaje():
#     print("Mensaje especial")
#     print("Estoy aprendiendo funciones")


# imprimir_mensaje()

# def comentario(mensaje):
#     print("Hola")
#     print("Como estas")
#     print(mensaje)
#     print("Adios")


# opcion = int(input("Elige un a opcion (1, 2, 3): "))
# if opcion == 1:
#     comentario("Eligiste la opciòn 1")
# elif opcion == 2:
#     comentario("Eligiste la opciòn 2")
# elif opcion == 3:
#     comentario("Eligiste la opciòn 3")
# else:
#     print("Elige una opciòn valida")        

# def suma(a, b):
#     print("Se suman dos numeros")
#     resultado = a + b
#     return resultado

# sumatoria = suma(1, 4)    
# print(sumatoria)

   
# contador = 1
# print(contador)  
# while contador < 10:
#     contador += 1
#     print(contador)
    
# for contador in range(100) :
#     print(contador)




# producto_a = 10
# producto_b = 5
# producto_c = 7

# menu = """ 
# SISTEMA DE IMVENTARIO JAVIER 😎😎😎

# ¿QUE PRODUCTO VAS A COMPRAR?

# 1 - Producto A
# 2 - Producto B
# 3 - Producto C
# 4 - RESUMEN

# ELIGE UNA OPCIÒN: """

# opcion = int(input(menu))

# if opcion == 1:
#     while producto_a > 5:
#         producto_a = producto_a -1
#         print(producto_a)
# elif opcion == 2:
#     while producto_b > 3:
#         producto_b -1
# elif opcion == 3:
#     while producto_c > 3:
#         producto_c -1                
# else:
#     print("Eligie una opciòn valida")        

def run():
    # for contador in range(1000):
    #     if contador % 2 != 0:
    #         continue
    #     print(contador)

    for i in range(10000):
        print(i)
        if i == 4567:
            break
    


if __name__ == "main":
    run()






