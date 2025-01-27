import random

A = random.randint(0,10)
B = random.randint(0,10)
print(A)
print(B)

salir = True

while salir:
    if A == B:
        A = random.randint(0,10)
        B = random.randint(0, 10)
    else:
        continue


