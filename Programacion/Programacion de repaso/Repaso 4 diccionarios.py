import random

letrasDni = ['T','R','W','A','G','M','Y','F','P','D','X','B','N','J','Z','S','Q','V','H','L','C','K','E']
numeros_telefono = ["612345678","698712345","634567890","677123456","645987321","659123789","621456987","638741256","690123654","673852190"]
nombres = ["Laura Fernández","Carlos Ruiz","Ana Torres","David Martínez","Marta López","Sergio Morales","Patricia Gómez","Iván Navarro","Elena Castillo","Jorge Sánchez"]
dnis = []

#clientes = {dni{"valor":nombre."valor2":telefono,"valor2":compras}}
clientes = {}


dnis = []

while len(dnis) < 10:
    numero = random.randint(10000000, 99999999)
    if numero not in dnis:
        letra = letrasDni[numero % 23]
        dni = f"{numero}{letra}"
        dnis.append(dni)

#print(dnis)
#print(dnis[1])

for i in range(10):
    long_dnis = len(dnis)
    long_nombres = len(nombres)
    long_tfn = len(numeros_telefono)
    dni = ""
    nombre = ""
    tfn = ""
    compras = []

    for j in range(random.randrange(1,6)):
        numero_random = random.randrange(100,1001)
        compras.append(numero_random)



    #dni
    numero_dni = int(random.randrange(long_dnis))
    #print(numero_dni)
    dni = dnis[numero_dni]
    #print(dni)
    dnis.remove(dnis[numero_dni])
    #print(dnis)

    #nombres
    numero_nombre = int(random.randrange(long_nombres))
    #print(numero_nombre)
    nombre = nombres[numero_nombre]
    #print(dni)
    nombres.remove(nombres[numero_nombre])
    #print(dnis)

    #tfns
    numero_tfn = int(random.randrange(long_tfn))
    #print(numero_tfn)
    tfn = numeros_telefono[numero_tfn]
    #print(tfn)
    numeros_telefono.remove(numeros_telefono[numero_tfn])
    #print(numeros_telefono)

    
    clientes[dni] = {"nombre": nombre, "tfn": tfn, "compras": compras}


    
#print(clientes)


titulo = "Clientes".center(70,"*") + "\n" + "Dni".ljust(15) + "Nombre".ljust(20) + "Telefono".rjust(15) + "Compras".rjust(20) + "\n" + "*"*70

print(titulo)
datos = ""

for dni in clientes:
    datos += str(dni).ljust(15) + str(clientes[dni]["nombre"]).ljust(20) +str(clientes[dni]["tfn"]).rjust(15)
    total_compras = 0
    for i in range(len(clientes[dni]["compras"])):
        total_compras = clientes[dni]["compras"][i]
        if i == 0:
            datos += str(clientes[dni]["compras"][i]).rjust(15) +"\n"
        else:
            datos += " ".ljust(50) + str(clientes[dni]["compras"][i]).rjust(15) +"\n"
    
    datos += "".center(70,"-") +"\n"
    datos += "Total Compras".ljust(50) + str(total_compras).rjust(12)+"\n"
    datos += "".center(70,"-") +"\n"


print(datos)
print(clientes)


lista_dnis = list(clientes.keys())
for pasada in range(len(lista_dnis)):
    for i in range(len(lista_dnis)-1-pasada):
        if lista_dnis[i] > lista_dnis[i+1]:
            aux = lista_dnis[i+1]
            lista_dnis[i+1] = lista_dnis[i]
            lista_dnis[i] = aux
for dni in lista_dnis:
    datos += str(dni).ljust(15) + str(clientes[dni]["nombre"]).ljust(20) +str(clientes[dni]["tfn"]).rjust(15)
    total_compras = 0
    for i in range(len(clientes[dni]["compras"])):
        total_compras = clientes[dni]["compras"][i]
        if i == 0:
            datos += str(clientes[dni]["compras"][i]).rjust(15) +"\n"
        else:
            datos += " ".ljust(50) + str(clientes[dni]["compras"][i]).rjust(15) +"\n"
    
    datos += "".center(70,"-") +"\n"
    datos += "Total Compras".ljust(50) + str(total_compras).rjust(12)+"\n"
    datos += "".center(70,"-") +"\n"


print(datos)


datos = ""
lista_dnis = list(clientes.keys())
for pasada in range(len(lista_dnis)):
    for i in range(len(lista_dnis)-1-pasada):
        if clientes[lista_dnis[i]]["nombre"] > clientes[lista_dnis[i+1]]["nombre"]:
            aux = lista_dnis[i+1]
            lista_dnis[i+1] = lista_dnis[i]
            lista_dnis[i] = aux
for dni in lista_dnis:
    datos += str(dni).ljust(15) + str(clientes[dni]["nombre"]).ljust(20) +str(clientes[dni]["tfn"]).rjust(15)
    total_compras = 0
    for i in range(len(clientes[dni]["compras"])):
        total_compras = clientes[dni]["compras"][i]
        if i == 0:
            datos += str(clientes[dni]["compras"][i]).rjust(15) +"\n"
        else:
            datos += " ".ljust(50) + str(clientes[dni]["compras"][i]).rjust(15) +"\n"
    
    datos += "".center(70,"-") +"\n"
    datos += "Total Compras".ljust(50) + str(total_compras).rjust(12)+"\n"
    datos += "".center(70,"-") +"\n"


print(datos)


datos = ""
lista_dnis = list(clientes.keys())
for pasada in range(len(lista_dnis)):
    for i in range(len(lista_dnis)-1-pasada):

        total_compras_i = 0
        total_compras_i_1 = 0
        for compra in clientes[lista_dnis[i]]["compras"]:
            total_compras_i += compra

        for compra in clientes[lista_dnis[i+1]]["compras"]:
            total_compras_i_1 += compra


        if total_compras_i > total_compras_i_1:
            aux = lista_dnis[i+1]
            lista_dnis[i+1] = lista_dnis[i]
            lista_dnis[i] = aux
for dni in lista_dnis:
    datos += str(dni).ljust(15) + str(clientes[dni]["nombre"]).ljust(20) +str(clientes[dni]["tfn"]).rjust(15)
    total_compras = 0
    for i in range(len(clientes[dni]["compras"])):
        total_compras = clientes[dni]["compras"][i]
        if i == 0:
            datos += str(clientes[dni]["compras"][i]).rjust(15) +"\n"
        else:
            datos += " ".ljust(50) + str(clientes[dni]["compras"][i]).rjust(15) +"\n"
    
    datos += "".center(70,"-") +"\n"
    datos += "Total Compras".ljust(50) + str(total_compras).rjust(12)+"\n"
    datos += "".center(70,"-") +"\n"


print(datos)