import random


def exercici1(opciones, excepciones):
    if type(opciones) != str:
        raise ValueError("The options have to be a string")

    if type(excepciones) != tuple:
        raise ValueError("The exceptions have to be a tuple")

    cont = 0
    for i in opciones:
        if i == ";":
            cont = cont + 1

    if cont < 2:
        raise ValueError("The minimun amount of options are 2")

    salir = False
    while salir == False:
        cont = 1
        opcion_actual = ""
        for i in opciones:
            if i == ";":
                print(str(cont) + ") " + opcion_actual)
                cont = cont + 1
                opcion_actual = ""

            else:
                opcion_actual = opcion_actual + i

        try:
            opcion = input("option: ")

            if not opcion.isdigit() and opcion not in excepciones:
                raise IndexError("The option is not a number and is not in exceptions")

            elif opcion in excepciones:
                for i in excepciones:
                    if str(i) == opcion:
                        print(i)
                        salir = True

            elif opcion.isdigit() and int(opcion) > cont or int(opcion) < 1 and opcion not in excepciones:
                raise IndexError("The option is out of range and not in exceptions")

            else:
                if int(opcion) <= 3 and int(opcion) >= 1:
                    print(int(opcion))
                    salir = True

        except IndexError as error:
            print(error)
            input("Enter to continue")


# options = "opcion1;opcion2;opcion3;"
# exceptions = ("A", "c")
#
# exercici1(options, exceptions)


def exercici2(*string):
    for i in string:
        if type(i) != str:
            raise TypeError("only string")

    if len(string) < 2:
        raise ValueError("There has to be more than 1 string")

    else:
        resultado = ""
        cont = 0
        for i in string:
            if cont == 0:
                resultado = resultado + i
                cont = cont + 1

            else:
                resultado = resultado + "-" + i

        print(resultado)


# exercici2("a", "b", "c")


def exercici3(asignatura, **parelles):
    if len(parelles) == 0:
        print(asignatura.center(78, "="))
        print("Code".ljust(30), "Midterm Exam".rjust(15), "Final Exam".rjust(15), "Average Grade".rjust(15))

    else:
        for i, j in parelles.items():
            if type(j) != list:
                raise ValueError("The values have to be a list of integers")
            elif not i[:2].isalpha() or not i[2:].isnumeric() or len(i) != 5:
                raise ValueError("The id have to have the format: two Letters + 3 numbers")
            elif len(j) != 2:
                raise AssertionError("The list have to contain only two floats")
            for z in j:
                if type(z) != float:
                    raise TypeError("Values in list have to be floats")

        print(asignatura.center(78, "="))
        print("Code".ljust(30), "Midterm Exam".rjust(15), "Final Exam".rjust(15), "Average Grade".rjust(15))

        total = 0
        average = 0
        for i, j in parelles.items():
            total = j[0] + j[1]
            midtherm = j[0]
            final = j[1]
            code = i
            total = round(total, 1)
            midtherm = round(midtherm, 1)
            final = round(final, 1)
            print(str(code).ljust(30), str(midtherm).rjust(15), str(final).rjust(15), str(total).rjust(15))
            average = average + total

        print("="*78)
        average = round(average, 1)
        print("Total Average".ljust(60), str(average/len(parelles)).rjust(18))


# exercici3("Maths", RT345=[7.12, 6.55], SW432=[5.44, 7.63])


def exercici4(lista1, lista2):
    resultado = []
    if len(lista1) == 0 and len(lista2) == 0:
        return resultado

    elif len(lista1) == 0 and len(lista2) != 0:
        resultado = exercici4(lista1, lista2[1:])
        return resultado

    elif len(lista1) != 0 and len(lista2) == 0:
        resultado = exercici4(lista1[1:], lista2)
        return resultado

    else:
        if lista1[0] in lista2:
            resultado = exercici4(lista1[1:], lista2)

            if lista1[0] not in resultado:
                resultado.append(lista1[0])
                return resultado

            else:
                return resultado

        else:
            resultado = exercici4(lista1[1:], lista2)
            return resultado


# longitud1 = random.randint(0, 10)
# longitud2 = random.randint(0, 10)
#
# lista1 = []
# lista2 = []
#
# for i in range(longitud1):
#     lista1.append(random.randint(1, 15))
#
# for i in range(longitud2):
#     lista2.append(random.randint(1, 15))
#
# resultado = exercici4(lista1, lista2)
#
# print(resultado)


def exercici5(lista1, lista2):
    resultado = []
    if len(lista1) == 0 and len(lista2) == 0:
        return resultado

    elif len(lista1) == 0 and len(lista2) != 0:
        resultado = exercici5(lista1, lista2[1:])
        if lista2[0] not in resultado:
            resultado.append(lista2[0])
        return resultado

    elif len(lista1) != 0 and len(lista2) == 0:
        resultado = exercici5(lista1[1:], lista2)
        if lista1[0] not in resultado:
            resultado.append(lista1[0])
        return resultado

    else:
        resultado = exercici5(lista1[1:], lista2[1:])
        if lista1[0] not in resultado and lista1[0] not in lista2:
            resultado.append(lista1[0])

        if lista2[0] not in resultado and lista2[0] not in lista1:
            resultado.append(lista2[0])

        return resultado


longitud1 = random.randint(0, 10)
longitud2 = random.randint(0, 10)

lista1 = []
lista2 = []

for i in range(longitud1):
    lista1.append(random.randint(1, 15))

for i in range(longitud2):
    lista2.append(random.randint(1, 15))

resultado = exercici5(lista1, lista2)

print(resultado)


def exercici6(num):
    hexadecimal = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, "A", "B", "C", "D", "E", "F"]
    resultado = ""

    if num < 16:
        resultado = str(hexadecimal[num])
        return resultado

    else:
        division = num % 16
        division = round(division, 0)
        resultado = exercici6(num//16) + str(hexadecimal[division])
        return resultado


print(exercici6(5132))