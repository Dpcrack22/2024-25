cadena = "DNI".ljust(15) + "Nombre".rjust(5)  +  "Nota".rjust(15) + "\n"
cadena = cadena + "*"*15 + "Alumnos".center(0) +  "*"*15 + "\n"
var1 = "11111111A"
var2 = "Pepe juan"
var3 = "4.3"
var1 = input("Dame tu DNI")
var2 = input("Dame tu Nombre")
var3 = input("Dame tu Nota")
cadena = cadena +  var1.ljust(15) + var2.rjust(5)  +  var3.rjust(15) + "\n"
Alumno = "Variable 1 = ¨{}, Variable 2 = {}, Variable 3 = {}".format(var1,var2,var3)
print(cadena)