comptador = 0

for num in range(1, 1001):
    if num % 7 == 0:
        comptador += 1
        print(num, end=" ")

print("\nHi ha {} múltiples de 7 entre 1 i 1000.".format(comptador))
