
while True:
    P = input("Introduce el numero de la Potencia activa (Ponga 0 si no tiene este dato): ")
    Q = input("Introduce el numero de la Potencia reactiva (Ponga 0 si no tiene este dato): ")
    S = input("Introduce el numero de la Potencia aparente (Ponga 0 si no tiene este dato): ")
    if not P.isdigit() or not Q.isdigit() or not S.isdigit():
        print("Por favor, introduce números válidos.")
    else:
        P = float(P)
        Q = float(Q)
        S = float(S)
        if P == 0 and Q == 0 and S == 0:
            print("Por favor, introduce al menos un valor distinto de cero.")
        elif :
            print("La potencia aparente debe ser mayor que la potencia activa y o la potencia reactiva.")
        else:
            if S == 0:
                S = (P**2 + Q**2)**0.5
                print("Potencia aparente: ",S)
                break
            elif P == 0:
                P = (S**2 - Q**2)**0.5
                print("Potencia activa: ",P)
                break
            elif Q == 0:
                Q = (S**2 - P**2)**0.5
                print("Potencia reactiva: ",Q)
                break
            else:
                print("Potencia activa: ", P)
                print("Potencia reactiva: ", Q)
                print("Potencia aparente: ", S)
                break

