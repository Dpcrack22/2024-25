# Inicializa una cadena 'llista' que contendrá los encabezados de la tabla de alumnos. 
# Se centra con 50 asteriscos arriba y abajo, y se definen los encabezados: DNI, Nombre, Nota, y Nota de boletín.
llista = "*"*50 + "\n" + "DNI".ljust(15) + "Nombre".ljust(15) + "Nota".ljust(5) + "Nota boletin".rjust(15) + "\n" + "*"*50 + "\n"

# Define el menú que se mostrará en pantalla con 3 opciones: agregar un nuevo alumno, mostrar todos los alumnos o salir.
menu = "1) Nuevo alumno\n2) Mostrar alumnos\n3) Salir"

# La variable 'salir' controla el bucle principal del programa. Inicialmente es False para mantener el bucle activo.
salir = False

# Bucle principal del programa que continuará hasta que 'salir' sea True.
while not salir:
    # Muestra el menú al usuario
    print(menu)
    # Solicita una opción al usuario, convirtiéndola a un número entero
    opcion = int(input("Opcion: "))

    # Opción 1: Añadir un nuevo alumno
    if opcion == 1:
        # Solicita los datos del alumno: DNI, nombre y nota
        DNI1 = input("\nIntroduce el DNI del Alumno: ")
        Alumne1 = input("\nIntroduce el Nombre del alumno: ")
        Nota1 = float(input("\nIntroduce la nota del alumno: "))  # Convierte la nota a un valor flotante
        
        # Dependiendo de la nota, se asigna un valor descriptivo para el boletín.
        if Nota1 < 5:
            Boletin = "Suspes"  # Suspenso
        elif 5 <= Nota1 < 6:
            Boletin = "Aprobat"  # Aprobado
        elif 6 <= Nota1 < 7:
            Boletin = "Be"  # Bien
        elif 7 <= Nota1 < 9:
            Boletin = "Notable"  # Notable
        else:
            Boletin = "Excelent"  # Excelente
        
        # Formatea los datos del alumno para añadirlo a la lista 'llista', alineando las columnas con 'format()'.
        # {2:5.2f} asegura que la nota se muestre con dos decimales.
        llista = llista + "{0:15}{1:15}{2:5.2f}{3:15}\n".format(DNI1, Alumne1, Nota1, Boletin)
    
    # Opción 2: Mostrar la lista de alumnos
    elif opcion == 2:
        print("\n" + llista)  # Imprime la lista completa de alumnos
    
    # Opción 3: Salir del programa
    elif opcion == 3:
        salir = True  # Cambia la variable 'salir' a True para salir del bucle y terminar el programa
    
    # Opción inválida: Si el usuario introduce una opción que no está en el menú
    else:
        print("Opción inválida (Marca un número de las opciones)")
