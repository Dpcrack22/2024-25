# Este programa permite gestionar un conjunto de clientes, mostrando su información
# y permitiendo ordenarlos por diferentes criterios: NIF, código numérico y total de compras.

# Diccionario que almacena la información de los clientes.
clientes = {
    "34343434A": {"nombre": "Teodoro", "codigo": "AFT3245", "tfn": 444444444, "compras": [234, 43, 567]},
    "54545454T": {"nombre": "Amaia", "codigo": "TSR8462", "tfn": 555555555, "compras": [1001, 34]},
    "12344123G": {"nombre": "Isidoro", "codigo": "NTZ4123", "tfn": 666666666, "compras": [2300, 340, 34, 123]},
    "62323455B": {"nombre": "Ines", "codigo": "UTN4875", "tfn": 123412344, "compras": [485, 568, 682, 456, 12]},
    "81238478S": {"nombre": "Soraya", "codigo": "TSX8245", "tfn": 939393933, "compras": [854]},
    "96345245J": {"nombre": "Carlos", "codigo": "VNP6438", "tfn": 542342342, "compras": [34, 645, 680]},
    "44234423U": {"nombre": "Ernesto", "codigo": "KSQ9345", "tfn": 636328284, "compras": [939, 34, 145]}
}

# Cabecera de la tabla que se mostrará al usuario
cabecera = (
    "Clientes".center(70, "=") + "\n" +
    "Nif".ljust(15) + "Nombre".ljust(15) +
    "Codigo".ljust(10) + "Tfn".ljust(10) +
    "Total Compras".rjust(15) + "\n" + "*" * 70
)

# Menú principal que presenta las opciones al usuario
menu0 = (
    "Client Search".center(20, "=") + "\n" +
    "1) Show clients ordered by NIF\n" +
    "2) Show clients ordered by numeric code\n" +
    "3) Show clients ordered by purchases\n" +
    "4) Exit\n"
)

# Flags para controlar el flujo del programa
flag0 = True  # Controla el bucle principal
flag00 = True  # Controla el bucle del menú principal
flag01 = False  # Controla el bucle de ordenación por NIF
flag02 = False  # Controla el bucle de ordenación por código numérico
flag03 = False  # Controla el bucle de ordenación por total de compras

# Bucle principal que controla la ejecución del programa
while flag0:
    # Bucle para mostrar el menú principal y obtener la opción del usuario
    while flag00:
        print(menu0)  # Imprime el menú en la consola
        opc = input("Choose an option: ")  # Solicita la opción al usuario
        # Validación de entrada para asegurarse de que se introduzca un número
        if not opc.isdigit():
            print("Only numerical option")
            input("Press Enter to continue")
        elif not int(opc) in range(1, 5):  # Verifica que la opción esté en el rango correcto
            print("Not in range option")
            input("Press Enter to continue")
        # Control de flujo basado en la opción seleccionada
        elif int(opc) == 1:
            flag01 = True  # Activar el bucle para mostrar clientes ordenados por NIF
            flag00 = False
        elif int(opc) == 2:
            flag02 = True  # Activar el bucle para mostrar clientes ordenados por código
            flag00 = False
        elif int(opc) == 3:
            flag03 = True  # Activar el bucle para mostrar clientes ordenados por total de compras
            flag00 = False
        elif int(opc) == 4:
            flag00 = False  # Salir del bucle del menú principal
            flag0 = False  # Terminar el programa

    # Ordenar por NIF
    while flag01:
        print(cabecera)  # Imprime la cabecera de la tabla
        datos = ""  # Inicializa la variable para almacenar los datos de los clientes
        # Convierte el diccionario de clientes a una lista de tuplas (NIF, datos del cliente)
        codigo = list(clientes.items())
        # Ordena la lista por NIF usando sort() con una función lambda
        codigo.sort(key=lambda x: x[0])  # Ordena usando el NIF como clave
        # Recorre los clientes ordenados para generar la salida
        for clave, items in codigo:
            # Calcula el total de las compras de cada cliente
            suma_ventas = sum(items["compras"])  # Sumar las compras directamente
            # Formatea la salida para cada cliente
            datos += clave.ljust(15) + items["nombre"].ljust(15) + str(items["codigo"]).ljust(10) + str(
                items["tfn"]).ljust(10) + str(suma_ventas).rjust(15) + "\n"
        print(datos)  # Imprime los datos formateados
        input("Press Enter to continue...")  # Espera que el usuario presione Enter
        flag00 = True  # Regresa al menú principal
        flag01 = False  # Termina el bucle de ordenación por NIF

    # Ordenar por código numérico
    while flag02:
        print(cabecera)  # Imprime la cabecera de la tabla
        # Convierte los valores del diccionario a una lista
        codigo = list(clientes.values())
        # Ordena por el código numérico extraído
        codigo.sort(key=lambda x: int(x["codigo"][3:7]))  # Asegura que se ordene por el número en el código
        datos = ""  # Inicializa la variable para almacenar los datos de los clientes
        # Recorre los clientes ordenados para generar la salida
        for item in codigo:
            suma_ventas = sum(item['compras'])  # Sumar las compras directamente
            # Formatea la salida para cada cliente
            datos += str(item['nombre']).ljust(25) + str(item['codigo']).rjust(10) + str(
                item['tfn']).rjust(10) + str(suma_ventas).rjust(15) + "\n"
        print(datos)  # Imprime los datos formateados
        input("Press Enter to continue...")  # Espera que el usuario presione Enter
        flag00 = True  # Regresa al menú principal
        flag02 = False  # Termina el bucle de ordenación por código

    # Ordenar por total de compras
    while flag03:
        print(cabecera)  # Imprime la cabecera de la tabla
        # Convierte el diccionario de clientes a una lista de tuplas
        codigo = list(clientes.items())
        # Ordena usando la suma de las compras como clave, de mayor a menor
        codigo.sort(key=lambda x: sum(x[1]["compras"]), reverse=True)
        datos = ""  # Inicializa la variable para almacenar los datos de los clientes
        # Recorre los clientes ordenados para generar la salida
        for clave, items in codigo:
            suma_ventas = sum(items["compras"])  # Sumar las compras directamente
            # Formatea la salida para cada cliente
            datos += clave.ljust(15) + items["nombre"].ljust(15) + str(items["codigo"]).rjust(10) + str(
                items["tfn"]).rjust(10) + str(suma_ventas).rjust(15) + "\n"
        print(datos)  # Imprime los datos formateados
        input("Press Enter to continue...")  # Espera que el usuario presione Enter
        flag00 = True  # Regresa al menú principal
        flag03 = False  # Termina el bucle de ordenación por compras
