"""Exercici 2 ( 1 punt )
Es crearà una funció amb el nom exercici2 que rebrà com a paràmetres entre 2 i n nombres enters
positius, i ens tornarà un float amb la mitjana dels números passats com a paràmetres.
Aquesta funció llançarà una excepció del tipus TypeError en cas que algun dels paràmetres que
passem no sigui un enter, mostrarà un missatge descriptiu de l'error i finalitzarà la seva execució.
És a dir si cridem a la funció com segueix:
print(exercici2())
print(exercici2(1))
Donarà un error del tipus TypeError i acabarà la seva execució
si cridem a la funció com segueix:
print(exercici2(“a”,1,2))
Llançarà una excepció del tipus TypeError, mostrarà un missatge descriptiu i n'acabarà l'execució.
si cridem a la funció com segueix:
print(exercici2(1,2))
ens tornarà un float amb la mitjana de 1 i 2.
print(exercici2(1,2,3))
ens tornarà un float amb la mitjana de 1, 2 i 3.
print(exercici2(1,2,3,4,5))
ens tornarà un float amb la mitjana de 1, 2, 3, 4 i 5.
"""

def exercici2(*nombres):
    try:
        if len(nombres) < 2:
            raise TypeError("At least two integers are required")
    except TypeError as e:
        return e
    
    try:
        suma = 0
        for numero in nombres:
            if type(numero) != int:
                raise TypeError(f"'{numero}' is not an integer")
            suma += numero
        return float(suma / len(nombres))
    except TypeError as e:
        return e
    
#print(exercici2())
#print(exercici2("a",1,2))
#print("" + "-"*50)
#print(exercici2(1,2,3.34))
#print(exercici2(1,2,3,4,5))


"""Exercici 4 ( 2 punts)
Es crearà una funció recursiva que rebrà un únic paràmetre "frase" i ens retornarà True o False
dependent de si
la frase passada és un palíndrom.Exemples de frases que són palíndroms:
Madam, I'm Adam.
A man, a plan, a canal: Panama!
Amore, Roma.
Emu love volume.
God lived as a devil dog.
Is it I, It is I!
Red rum, sir, is murder.
És a dir, cal eliminar tots els espais i tots els signes de puntuació abans de comprovar si la frase és
un palíndrom.
llista_signes_puntuacio = [" ",".",",","!","'"]
"""

def exercici4(frase):
    resultado = ""
    llista_signes_puntuacio = [" ",".",",","!","'"]
    for i in llista_signes_puntuacio:
        frase = frase.replace(i,"").lower()

    if len(frase) <= 1:
        return True
    if frase[0] != frase[-1]:
        return False
    return exercici4(frase[1:-1])

    

#print(exercici4("Is it I, It is I!"))



"""
Exercici 5 ( 2 punts).
Es crearà una funció recursiva que rebrà com a paràmetres únicament un número “num” i una base
“b” més petita que 10.
La funció retornarà un string amb el número “num” expressat a la base “b”.
Per canviar un nombre de base, s'han de fer divisions successives i després quedar-se amb els
residus i el darrer quocient.
Per exemple, per canviar 768 a base 8.
Vol dir que 768 expressat en base 8 seria 1400.
Para cambiar 853 a base 7:
I el resultat seria 2326. Vol dir que 853 expressat en base 7 seria 2326
Per comprovar si el resultat és correcte, podeu fer servir la següent funció iterativa que realitza el
mateix.
def changeBase(num,base):
 resultado = ""
 while num >= base:
 resultado = str(num%base) + resultado
 num = int(num/base)
 resultado = str(num) +resultado
 return resultado
 """
def exercici5(num,base):
    try:
        if base >= 10:
            raise ValueError("Base must be less than 10")
    except ValueError as e:
        return e
    
    if num < base:
        return str(num)
    else:
        return exercici5(num // base, base) + str(num % base)
    
print(exercici5(768,8))

