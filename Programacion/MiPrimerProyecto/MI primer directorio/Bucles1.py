"""
num = 1
while num%10!=0:
    num = int(input("Dame un multiplo de 10: "))
    if not num%10==0:
        print("No has introduit un multiplo de 10")
print("Has introduit {}".format(num))


El bucle while se puede usar como en esta ocasion en esta ocasion lo que estamos haciendo es lo siguiente:
 Estamos diciendo que en num debemos de escribir un multiplo de 10 si no se hace eso se repite el programa hasta que pongas el multiplo
"""

for i in range(10): #Con esto hacemos el bucle para repetir 10 veces i = el numero de veces
    print("i = {}".format(i))
    if i == 2: #Con esto hacemos que continue y siga al siguiente comando si es dos
        continue
    if i == 5: #Con esto hacemos que si i = 5 se rompa y se termine
        break