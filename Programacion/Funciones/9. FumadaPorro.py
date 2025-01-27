def listas_iguales(a,b,c):
    if len(a)%2==0:
        print("")
    else:
        if len(c) == 0:
            c.append(a[-1])
            a.remove(a[-1])

        if len(b) == 0:
            b.append(a[-1])
            a.remove(a[-1])

        if b[-1] > c[-1]:
            b.append(c[-1])
            c.remove(c[-1])

        if len(c) != 0:
            c.append(b[-1])
            b.remove(b[-1])


        listas_iguales(a,b,c)
print("")
print(listas_iguales(a=[5,4,3,2,1],b=[], c=[]))
