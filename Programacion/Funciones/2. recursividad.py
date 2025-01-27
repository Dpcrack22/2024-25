from statistics import median


def funcion_multiplicacion(a,b=1):
    print(a)
    print(b)
funcion_multiplicacion(2)

def funcion_multiplicacion(a,b=1):
    print(a)
    print(b)
funcion_multiplicacion(2,10)

#!!!!!!!!!!!!!!!!!!! Para Examen CUIDADO !!!!!!!!!!!!!!!!!!!!!!!!!!!#
                    #Parametros Arbitrarios#
def funcion_ejemplo(a,b,*c):
    print(a)
    print(b)
    print(c)
funcion_ejemplo(1,2,3,4,5,"asdsa","sadaf",True)

# def funcion_ejemplo(a,b,*c,d): #En este caso la d no se podra usar porque decimos que a partir de la "c" todo sera una tupla
#
#     print(a)
#     print(b)
#     print(c)
# funcion_ejemplo(1,2,3,4,5,"asdsa","sadaf",True)

def numeros_infinitos(a,b,**c):
    print(a)
    print(b)
    print(c)
numeros_infinitos(1,2,clave1="valor1", clave2 = 3)


def funcion_ejemplo(a,b,*c):
    suma = a + b
    for numero in c:
        suma += numero
    media = suma/(2+len(c))
    return media
print(funcion_ejemplo(1,2,3,56,6,5,3,2,4,56,7))

def funcion_menucito(titulo="",*opciones):
    menu = ""
    if titulo != "":
        print(titulo.center(10, "*"))
    for i in range(len(opciones)):
        menu += str(i+1)+")"+opciones[i]+"\n"

    while True:
        print(menu)
        opc = input("Opcion: ")
        if not opc.isdigit():
            print("numeros gracias")
        elif int(opc) not in range(1, len(opciones) + 1):
            print("Opcion fuera de rango chato")
        else:
            opc = int(opc)
            return opc
funcion_menucito("Titulo","Opcion1","Opcion2","Opcion2")

