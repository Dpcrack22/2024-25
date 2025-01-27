while True:
    try:
        numero = int(input("Introduce un número múltiple de 10: "))

        if numero % 10 != 0:
            print("El número no es múltiple de 10. Inténtalo de nuevo.")
        else:
            break

    except ValueError:
        print("Por favor, introduce un número entero.")

coeficiente = numero // 10
exponente = 1

while numero % 10 == 0:
    numero //= 10
    exponente += 1

print("{} per 10 elevat a {}".format(coeficiente, exponente - 1))
