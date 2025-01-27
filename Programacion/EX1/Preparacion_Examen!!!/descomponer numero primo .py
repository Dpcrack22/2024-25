# Inicializamos una variable booleana 'primo', aunque no es usada en este código.
primo = True

# Pedimos al usuario un número entero para descomponer.
num = int(input("Dame un numero: "))
num1 = num  # Guardamos el valor original del número para mostrarlo al final.
descomposicion = ""  # Variable que almacenará el resultado de la descomposición.

# Bucle para probar la divisibilidad desde 2 hasta num // 2.
# El bucle debe empezar en 2, no en 3, ya que queremos también considerar el número 2 como factor.
for i in range(2, num // 2 + 1):
    
    # Bucle para dividir el número por el valor de i tantas veces como sea divisible por i.
    while num % i == 0:  # Mientras el número sea divisible por i...
        num = num // i  # Dividimos el número por i.
        
        # Si no es el último factor, añadimos el factor i y un asterisco al resultado.
        if num != 1:
            descomposicion = descomposicion + str(i) + "*"
        else:
            descomposicion = descomposicion + str(i)  # Si es el último factor, solo añadimos el número.

# Imprimimos el resultado de la descomposición.
print("Descomposición de {} = {}".format(num1, descomposicion))
