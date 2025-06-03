def exercici1(tupla,exceptions):
    """
    ValueError si la tupla d'opcions no és una tupla, amb el missatge associat "The options have to be a tuple"
    ZeroDivisionError si la tupla d'excepcions no és una tupla, amb el missatge associat "The exceptions have to be a tuple"
    FileNotFoundError si la tupla d'opcions no té com a mínim 2 elements, amb el missatge associat "The minimun length of the options are 2".
    I en qualsevol daquests 3 casos, la funció finalitzarà.
    """

    try:
        if type(tupla) != tuple:
            raise ValueError("The options have to be a tuple")
        
    except ValueError as e:
        
        return e

    try:
        if type(exceptions) != tuple:
            raise ZeroDivisionError("The exceptions have to be a tuple")
        
    except ZeroDivisionError as e:
        
        return e
    
    try:
        if len(tupla) < 3:
            raise FileNotFoundError("The minimun length of the options are 2")
        
    except FileNotFoundError as e:
        
        return e
    
    

    while True:
        for i in range(len(tupla)):
            print("{}) {}".format(i + 1,tupla[i]))
            
        opcion = input("Opcion: ")
        try:
            if not opcion.isdigit() and not opcion in exceptions:
                raise TypeError("The option is not a number and is not in exceptions")
            if opcion.isdigit():
                opcion = int(opcion)
                if opcion not in range(1, len(tupla) + 1):
                    raise TypeError("The option is out of range and not in exceptions")
            else:
                if opcion not in exceptions:
                    raise TypeError("The option is not a number and is not in exceptions")
                else:
                    if opcion in exceptions:
                        return opcion
                    else:
                        return int(opcion)
        except TypeError as e:
            print(e)
            input("Enter to continue")
    


        




#tupla=("opcio1","opcio2","opcion3")
#lista=["opcio1","opcio2","opcio3"]
#print(exercici1(tupla,exceptions=("c","d",10)))

#print(len(tupla))

"""
Exercici 3 (2,5 punts)
Es crearà una funció amb el nom exercici3. Aquesta funció rebrà com a mínim 1 paràmetre que es
dirà títol.
Si cridem a la funció com segueix:
exercici3("Titol")
ens imprimirà:
i no retornarà res.
També podrà rebre tantes parelles com vulguem del tipus:
id=[sencer1,sencer2]
on sencer1 representarà la quantitat de productes i sencer2 representarà el preu per unitat.
Les parelles del tipus id=[sencer1,sencer2] representaran els productes d'una compra.
Si cridem a la funció com segueix:
exercici3("Titol",RT345=[2,145])
Ens mostrarà la següent taula:
Si cridem a la funció com segueix:
exercici3("Titol",RT345=[2,145],SW432=[5,549])
Ens mostrarà la següent taula:
Si cridem a la funció com segueix:
exercici3("Titol",RT345=[2,145],SW432=[5,549],OT441=[4, 299])
Ens mostrarà la següent taula:
Aquesta funció llençarà excepcions del tipus:
ValueError en el cas que els valors passats com id=valor, no sigui una llista mostrarà el missatge
associat
"The values have to be a list of integers"
I finalitzarà la seva execució.
AssertionError en el cas que els valors continguts a la llista que es passa com a valor no tingui
longitud 2, mostrarà el missatge associat
"The list have to contain only two integers" i finalitzarà la seva execució.
TypeError en el cas que un dels dos valors continguts a la llista que es passa com a valor no siguin
sencer, mostrarà el missatge associat
"Values in list have to be integers" i finalitzarà la seva execució.
"""

def exercici3(titulo="", **opciones):
    
    try:
        id = list(opciones.keys())
        for i in range(len(opciones)):
            if not type(opciones[id[i]]) == list:
                raise ValueError("The values have to be a list of integers")
            if len(opciones[id[i]]) != 2:
                raise AssertionError("The list have to contain only two integers")
            if not (opciones[id[i]][0] == int(opciones[id[i]][0]) and opciones[id[i]][1] == int(opciones[id[i]][1])):
                raise TypeError("Values in list have to be integers")
    except ValueError as e:
        return e
    except AssertionError as e:
        return e
    except TypeError as e:
        return e
    
    datos = ""
    datos += titulo.center(100, "=") + "\n"
    datos += "Items".ljust(15) + "Amount".rjust(60) + "Price".rjust(15) + "Total".rjust(10) + "\n"
    
    for i in range(len(opciones)):
        id = list(opciones.keys())[i]
        cantidad = opciones[id][0]
        precio = opciones[id][1]
        total = cantidad * precio
        
        datos += id.ljust(15) + "{}".rjust(60).format(cantidad) + "{}".rjust(15).format(precio) + str(total).rjust(10) + "\n"

    total_items = 0
    for i in range(len(opciones)):
        id = list(opciones.keys())[i]
        cantidad = opciones[id][0]
        precio = opciones[id][1]
        total_items += cantidad * precio
    
    

        


    datos += "=" * 100 + "\n" + "Items".ljust(15) + "{}".rjust(83).format(total_items) + "\n"

    return datos



print(exercici3("Titol",RT345=[2,145],SW432=[5,549],OT441=[4, 299]))