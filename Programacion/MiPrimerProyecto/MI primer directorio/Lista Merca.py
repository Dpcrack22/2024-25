# Cabecera
llista = "Producto".ljust(15) + "Cantidad".ljust(10) + "Precio". ljust(10) + "Total". ljust(10) + "\n"
llista += "Mercadona".center(45, "*") + "\n"

# Producto 1
NProducto1 = input ("\nIntrodueix el nom del producte: ") # Para introducir datos del nombre del producto
CProducto1 = int(input("Introdueix la cantitat del producte: ")) # Para introducir la cantidad del producto
PProducto1 = float (input("Introdueix preu del producte: ")) # Para introducir precio del producto
totalProducto1 = CProducto1 * PProducto1 # Total del precio por producto x cantidad
llista += "{0:15}{1:<10}{2:<10.3f}{3:<10.2f}\n".format(NProducto1, CProducto1, PProducto1, totalProducto1)

# Producto 2
NProducto2 = input ("\nIntrodueix el nom del producte: ")
CProducto2 = int(input("Introdueix la cantitat del producte: "))
PProducto2 = float (input("Introdueix preu del producte: "))
totalProducto2 = CProducto2 * PProducto2
llista += "{0:15}{1:<10}{2:<10.3f}{3:<10.2f}\n".format(NProducto2, CProducto2, PProducto2, totalProducto2)

# Producte 3
NProducto3 = input("\nIntrodueix el nom del producte: ")
CProducto3 = int(input("Introdueix la cantitat del producte: "))
PProducto3 = float(input("Introdueix preu del producte: "))
totalProducto3 = CProducto3 * PProducto3
llista += "{0:15}{1:<10}{2:<10.3f}{3:<10.2f}\n".format(NProducto3, CProducto3, PProducto3, totalProducto3)
llista += "*" * 45 + "\n"

# Resultado
llista += ("Total: " + "{0:.2f}". format (totalProducto1 + totalProducto2 + totalProducto3)).rjust(45)
print ("\n" + llista)
