"""
primo = True
num = int(input("Dame un numero: "))

for i in range(2,num//2):
    if  num%i == 0:
        primo = False
        break
if primo:
    print("Es primo")
else:
    print("No es primo ")
"""
primo = True
for j in range(1,12):
    num = j
    primo = True
    for i in range(2,num//2):
        if  num%i == 0:
            primo = False
            break
    if primo:
        print("Es primo")
        break