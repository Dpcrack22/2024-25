menu ="\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n" +  "Seleccione una opción:" + "\n" + "1) Sumar" + "\n" + "2) Restar" + "\n" + "3) Multiplicar" + "\n" + "4) Dividir" + "\n" + "0) Salir"

while True:

    print(menu)

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        num1 = float(input("Introduce el primer número: "))
        num2 = float(input("Introduce el segundo número: "))
        print("La suma de {} + {} es: {}".format(num1, num2, num1 + num2))
        input("Presiona cualquier tecla para continuar...")

    elif opcion == "2":
        num1 = float(input("Introduce el primer número: "))
        num2 = float(input("Introduce el segundo número: "))
        print("La resta de {} - {} es: {}".format(num1, num2, num1 - num2))
        input("Presiona cualquier tecla para continuar...")

    elif opcion == "3":
        num1 = float(input("Introduce el primer número: "))
        num2 = float(input("Introduce el segundo número: "))
        print("El producto de {} * {} es: {}".format(num1, num2, num1 * num2))
        input("Presiona cualquier tecla para continuar...")

    elif opcion == "4":
        num1 = float(input("Introduce el primer número: "))
        num2 = float(input("Introduce el segundo número: "))
        if num2 == 0:
            print("Error: No se puede dividir entre 0.")
        else:
            print("La división de {} / {} es: {}".format(num1, num2, num1 / num2))
        input("Presiona cualquier tecla para continuar...")

    elif opcion == "0":
        print("Saliendo del programa...")
        break

    else:
        print("Opción no válida. Intente de nuevo.")
        input("Presiona cualquier tecla para continuar...")
