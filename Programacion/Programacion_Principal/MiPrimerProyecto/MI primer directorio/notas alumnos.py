#Cabecera
from cgi import print_environ_usage

llista = "*"*50 + "\n" + "DNI".ljust(15) + "Nombre".ljust(15) + "Nota". ljust(5) + "Nota boletin". rjust(15) + "\n" + "*"*50 + "\n"

#Alumnos
DNI1 = input("\n Introdueix el DNI del Alumne")
Alumne1 = input("\n Inrodueix el Nom del alumne")
Nota1 = float(input("\n INtrodueix la nota del alumne"))
if Nota1 <5:
    Boletin = ("Suspes")
elif 5<= Nota1 <6:
    Boletin = ("Aprobat")
elif 6<= Nota1<7:
    Boletin = ("Be")
elif 7<= Nota1<9:
    Boletin = ("Notable")
else :
    Boletin = ("Excelent")
llista = + "{0:15}{1:<15}{2:<5.3f}{3:<15.2f}\n".format(DNI1, Alumne1, Nota1, Boletin) #El dos f sirve para los decimales



DNI2 = input("\n Introdueix el DNI del Alumne")
Alumne2 = input("\n Inrodueix el Nom del alumne")
Nota2 = input("\n INtrodueix la nota del alumne")
NotaTotal2 =("")

DNI3 = input("\n Introdueix el DNI del Alumne")
Alumne3 = input("\n Inrodueix el Nom del alumne")
Nota3 = input("\n INtrodueix la nota del alumne")
NotaTotal3 =("")

print ("\n" + llista)
