#
menu = "Opcion1;Opcion2;Opcion3;Salir;"
def devuelve_opciones(menu):
    cadena_menu = ""
    total_opciones = menu.count(";")
    inicio = 0
    final = 0
    for i in range(total_opciones):
        opcion_iesima = ""
        if i == 0:
            inicio = 0
            final = menu.find(";")
            opcion_iesima = menu[inicio:final]

        else:
            inicio = final + 1
            final = menu.find(";",inicio)
            opcion_iesima = menu[inicio:final]
        
        cadena_menu += str(i+1)+ ")" + opcion_iesima + "\n"


    while True:
        print(cadena_menu)
        opcion = input("Selecciona una opción: ")
        if not opcion.isdigit():
            print("Solo se permiten opciones numéricas.")
            continue
        elif not int(opcion) in range(1, total_opciones + 1):
            print("Opción no válida. Debe estar entre 1 y", total_opciones)
            continue
        else:
            opcion = int(opcion)
            return opcion


            
        
#print(devuelve_opciones(menu))


#Media en tupla de entre 3 y x elementos
def media_tupla(x):
    if len(x) < 3:
        return "La tupla debe tener al menos 3 elementos."
    
    suma = 0
    for i in range(2, len(x)):
        suma += x[i]
    
    media = suma / (len(x) - 2)
    return media

print(media_tupla((4, 5)))


