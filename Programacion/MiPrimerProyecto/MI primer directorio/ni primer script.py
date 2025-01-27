from operator import truediv
from statistics import variance
from unittest.mock import right

print("Hola Mundo")
#Una variable es algo- que nos sirve para almacenar cosas
Variable1 = 25
Variable2 = "Hola mundo"
Variable3 = True
Variable4 = 66.34

print(Variable1)
print(Variable2)
print(Variable3)
print(Variable4)
print(type(Variable1))
#EL type sirve para saber de que tipo es la variable en la q estamos usabdo hay varios types

#VARIABLES TIPO STRING O CADENA
Variable5 = "Soy un string o cadena".rjust(30)
print(Variable5)
#Caracteres no imprimibles
#\n sirve para que el texto haga un salto de linea
#\d Hace que el texto tabule
#Si se añade al final del string .rjust o ljust con su respectivo numero pone un margen depeniendo el lado que has puesto
#El .center despues del string lo q hace es centrar el texto depeniedno los caracteres q pongas
#Si en un center se le añade de esta manera .center(50, "*") los espacios se cambiaran por la letra o caracter q pongas en este caso el asterisco
#Se pueden sumar o mejor dicho concadenar los strings de distintas variables
#Se puede hacer q un caracter se multiplique poniendo lo siguiente
Variable6 = "X"*50
print(Variable6)

#Ejercicio

DNI = "47894186K".ljust(15)
NOM = "David".ljust(20)
COGNOMS = "Perera González".ljust(50)
NOTA = "X".rjust(10)
Variables = (DNI, NOM, COGNOMS, NOTA)
print(Variables)

cadena = "Alumnos".center(95,"*") + "\n"
Cadena = cadena + "DNI".ljust(15) + "NOM".ljust(20) + "COGNOMS".ljust(50) + "NOTA".rjust(10)
print(Cadena)