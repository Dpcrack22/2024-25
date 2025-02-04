quants_numeros = int(input("Quants números vols introduir? "))

suma = 0
menor = None
major = None

for i in range(quants_numeros):
    num = int(input("Introdueix el número {}: ".format(i + 1)))
    suma += num
    
    if menor is None or num < menor:
        menor = num
    if major is None or num > major:
        major = num

mitjana = suma / quants_numeros

print("El número menor és: {}".format(menor))
print("El número major és: {}".format(major))
print("La mitjana dels números és: {:.2f}".format(mitjana))
