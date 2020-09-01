

# contador = 1
# print(contador)
# while contador < 10000:
#     contador += 1
#     print(contador)  

# for i in range(6):
#         if i == 5:
#             print("Figaroooo")
#             break
#         print("Galileo")

def run():
    comentario = input("Ingrese un comentario: ")
    for key_word in comentario:
        if key_word == "i":
            continue
        valor = key_word
        print(valor)

        
# Entry point
if __name__ == "__main__":
    run()