# cadena="Esto es una cadena"
# cadena1 ="Estoesunacadena"
# print(cadena.isalpha())
# print(cadena1.isalpha())
#
# # El usuario pide nombres i apellidos y saber si no hay numeros
# nombre = input("Dame un nombre y apellido")
# print((nombre.replace(" ", "").isalpha()))
from token import AMPER

# Sub cadenas
# cadena = "Esto es un string"
# print(cadena[5:9:2])

# Cadena = "Paco;Pepe;David;Fernando;"
# Contacto = "Xavier"
# ini = 0
# fin = 0
# insert_name = False
#
# for i in range(Cadena.count(";")):
#     if i == 0:
#         fin = Cadena.find(";")
#     else:
#         ini = fin + 1
#         fin = Cadena.find(";", ini)
#     if Contacto > Cadena[ini:fin]:
#         Cadena = Cadena[:ini]+Contacto+";"+Cadena[ini:]
#         insert_name = True
#         break
#
# if not insert_name:
#     Cadena = Cadena + Contacto + ";"
# #print(Cadena[ini:fin])
# print(Cadena)



# Cadena = "Paco-Alonso Fernandez:66666666;Pepe-Perera Gonzalez:66667777;David-Sanchez Navarro:6005760064;Fernando-Ruiz Angel:77677666;"
# Contacto = input("Dame un nombre:") + "-" + input("Dame tus apellidos") + ":" + input("Dame tu numero") + ";"
# ini = 0
# fin = 0
# insert_name = False
#
# for i in range(Cadena.count(";")):
#     for j in range(Cadena.count("-")):
#         if i == 0:
#             fin = Cadena.find(";")
#         else:
#             ini = fin + 1
#             fin = Cadena.find(";", ini)
#         if Contacto > Cadena[ini:fin]:
#             Cadena = Cadena[:ini]+Contacto+Cadena[ini:]
#             insert_name = True
#             break

# if not insert_name:
#     Cadena = Cadena + Contacto
#print(Cadena[ini:fin])
# print(Cadena)









# ini = 0
# fin = Cadena.find(";")
# print(Cadena[ini:fin])
#
# ini = fin + 1
# fin = Cadena.find(";")
# print(Cadena[ini:fin])
# ini = 0
# fin = Cadena.find(";")
#
# for i in range(4):
#     if i == 0:
#         ini = 0
#         fin = Cadena.find(";")
#         print(Cadena[ini:fin])
#     else:
#         ini = fin + 1
#         fin = Cadena.find(";", ini)
#         print(Cadena[ini:fin])


#print(Cadena[Cadena.find(";")+1:Cadena.find(";", Cadena.find(";")+1)])
# print(Cadena[0:4])
# print(Cadena[5:9])
# print(Cadena[10:15])
# print(Cadena[16:23])

#Hacer menu para un nuevo contacto, mostrar contactos, encontrar contactos y dentro de mostrar contactos poner un submenu de
# mostrar contactos odenados por nombre otro por odenados por apellido y otro que sea por numero y en el dubmenu de encontrar #
# contacto lo mismo por nombre apellido o telefono
# En el nombre debemos de hacer que nos busque por ejemplo elena con el o ena
#Indicaciones para el ejercicio
#

#Operador simple y util:  in  como print("to" in cadena)

#Practica nombres ordenados agenda

Agenda = "Paco-Alonso Fernandez:66666666;Pepe-Perera Gonzalez:66667777;David-Sanchez Navarro:6005760064;Fernando-Ruiz Angel:77677666;"
new_agenda = ""
ini = 0
fin = 0
for i in range(Agenda.count(";")):
    if i == 0:
        ini = 0
        fin = Agenda.find(";")
        new_agenda = Agenda[ini:fin] + ";"

    else:
        ini = fin + 1
        fin = Agenda.find(";",ini)

        new_ini = 0
        new_fin = 0
        len_new_agen = len(new_agenda)
        for j in range(new_agenda.count(";")):
            if j == 0:
                new_ini = 0
                new_fin = new_agenda.find(";")
            else:
                new_ini = fin + 1
                new_fin = Agenda.find(";", new_ini)
            old_name = Agenda[ini:fin][:Agenda[ini:fin].find("-")]
            name_new_agenda = new_agenda[new_ini:new_fin][:new_agenda[new_ini:new_fin].find("-")]
            print("Comparamos {} con {}".format(old_name,name_new_agenda))
            if old_name < name_new_agenda:
                new_agenda = new_agenda[:new_ini] + Agenda[ini:fin] + ";" + new_agenda[new_ini:]
                break


        if len_new_agen == len(new_agenda):
            print("Insertamos cantacto al final")
            new_agenda = new_agenda + Agenda[ini:fin] + ";"
    print(new_agenda)

    #print(Agenda[ini:fin])
