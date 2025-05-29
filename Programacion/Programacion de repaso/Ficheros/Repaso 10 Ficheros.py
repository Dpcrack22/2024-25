fichero = open("fichero.txt")

print(fichero.read())
#for linea in fichero:
 #   print(linea)

fichero.readline()  # Lee una línea del fichero

fichero.readlines()  # Lee todas las líneas del fichero y las devuelve como una lista
fichero.close()

# sin sobrescribir el fichero sin append
ficherito = open("fichero.txt", "r+")  
fichero.read()  # Lee todo el contenido del fichero
ficherito.write("Nueva línea añadida al fichero")  # Añade una nueva línea al final del fichero