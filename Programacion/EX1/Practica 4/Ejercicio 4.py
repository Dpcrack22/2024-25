QuantitatDiners= float(input("Donam la quantitat de diners (capital inicial): "))
TassaInteres = float(input("Donam una tassa d'interes (en %): "))
NombreAnys = int(input("Donam un numero d'anys: "))

CN = QuantitatDiners * (1 + TassaInteres / 100) ** NombreAnys

print("La quantitat de diners a pagar despres de {} anys es de {:.2f} unitats".format(NombreAnys, CN))