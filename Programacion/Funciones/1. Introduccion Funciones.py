# def saludo():
#     print("Hola Como estas")
#
# def multiplicar(paramentro1,parametro2):
#     return paramentro1 * parametro2
#
# var1 = multiplicar(20,10)
# print(var1)
#
# lista = [1,2,3,4]
# def medialista(lista):
#     suma = 0
#     for i in range(len(lista)):
#         suma += lista[i]
#     media = suma/len(lista)
#     return media
#
# media = medialista(lista)
# print(media)
#
# listaa = [1,2,3]
# def test(litaa):
#     listaa.append(100)
#     print("Adios")
#
# test(listaa)
# print(listaa)

menu00 = ("Opcion1","Opcion2","Opcion3","Opcion4")
def menus(tupla):
    menu = ""
    for i in range(len(tupla)):
        menu += str(i+1)+")"+tupla[i] + "\n"
    while True:
        print(menu)
        opc = input("Dame una opcion: ")
        if not opc.isdigit():
            print("Only numerical Options")
            input("Retry: ")
        else:
            if int(opc) not in range(1,len(tupla)+1):
                print("Opcion out of range:")
                input("Retry: ")
            else:
                return int(opc)


opcion = menus(menu00)
print(opcion)
menus(menu00)