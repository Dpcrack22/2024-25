def miBurbuja(lista,order="desc"):
    for pasadas in range(len(lista)-1):
        cambio = False

        for i in range(len(lista)-1-pasadas):

            if order == "desc":
                if lista[i] < lista[i+1]:
                    cambio = True
                    aux = lista[i]
                    lista[i] = lista[i+1]
                    lista[i+1] = aux
            else:
                if lista[i] > lista[i + 1]:
                    cambio = True
                    aux = lista[i]
                    lista[i] = lista[i + 1]
                    lista[i + 1] = aux
        if not cambio:
            return
