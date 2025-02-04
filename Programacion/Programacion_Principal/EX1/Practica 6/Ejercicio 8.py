numero = int(input("Introdueix un número: "))
divisors = ""

print("Els divisors de {} són:".format(numero))
for i in range(1, numero + 1):
    if numero % i == 0:
        divisors = str(i)
        print(divisors)
