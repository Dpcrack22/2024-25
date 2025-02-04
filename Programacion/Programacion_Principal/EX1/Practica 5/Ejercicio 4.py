any = int(input("Introdueix un any: "))

if (any % 4 == 0 and any % 100 != 0) or (any % 400 == 0):
    print("L'any {} és un any de traspàs.".format(any))
else:
    print("L'any {} no és un any de traspàs.".format(any))
