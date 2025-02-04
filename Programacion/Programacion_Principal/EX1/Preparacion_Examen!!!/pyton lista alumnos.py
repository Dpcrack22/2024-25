cadena = "Alumnos".center(95,"*") + "\n"
cadena = cadena + "DNI".ljust(15) + "NOM".ljust(20) + "COGNOMS".ljust(50) + "NOTA".rjust(10) + "\n"
cadena += "*"*96 + "\n"
cadena = cadena + "11111111A".ljust(15) + "Pepe".ljust(20) + "Lopez Gimeno".ljust(50) + "4,68".rjust(10) + "\n"
cadena = cadena + "22222222B".ljust(15) + "Nora".ljust(20) + "Ruiz Castellon".ljust(50) + "5,25".rjust(10) + "\n"
print(cadena)

Variable1 = "Texto1"
Variable2 = "Texto2"
print(Variable1,end="*", sep="-")
print(Variable2)