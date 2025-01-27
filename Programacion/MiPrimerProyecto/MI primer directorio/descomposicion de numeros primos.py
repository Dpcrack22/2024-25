primo = True
num = int(input("Dame un numero"))
num1 = num
descomposicion = ""
#operaciones
#Comparaciones

for i in range(3,num//2):
    while num%i==0:
        num = num/i
        if num !=1:
           descomposicion = descomposicion + str(i)+"*"

    else:
         descomposicion = descomposicion + str(i)
         break
print("Descomposicion de {} = {}".format(num1,descomposicion))