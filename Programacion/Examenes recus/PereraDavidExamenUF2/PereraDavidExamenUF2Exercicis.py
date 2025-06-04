"""Exercici 1 (2,5 punts):
Crearem una funció pagament_irpf(brut,trams) que ens servirà per calcular quant hem de pagar
d'irpf segons els trams.
Aquesta funció rebrà dos arguments; el primer serà el nostre sou brut i el segon serà un diccionari
que ens dirà per a cadascun dels trams el percentatge del nostre sou brut que hem de pagar.
Aquesta funció comprovarà que els arguments passats són correctes. Si l'argument trams no és un
diccionari, s'aixecarà una excepció del tipus NameError amb el missatge següent:
"the second argument must be a dictionary"
Si l'argument brut no és un enter, s'aixecarà una excepció del tipus TypeError amb el missatge
següent:
"the first argument must be a integer"
Si alguna de les claus del diccionari trams no és un enter s'aixecarà una excepció del tipus
ValueError amb el missatge següent:
"There is a key that is not a integer"
Si algun dels valors del diccionari trams no és un enter s'aixecarà una excepció del tipus
ValueError amb el missatge següent:
"There is a value that is not a integer"
Atès que un diccionari no té ordre, primer de tot haurem de trobar alguna manera d'ordenar les claus
del nostre diccionari trams, fent servir el mètode de la bombolla, i després a partir d'aquí anirem
calculant quant hem de pagar d'IRPF segons els trams.
Aquesta funció retornarà un float amb el valor de l'IRPF que hem de pagar.
Deixem el diccionari que ens serveix per calcular el pagament de l’irpf.
trams = {12450:19,299999:45,35199:30,59999:37,20199:24,300000:47}
Com exemple, si cobrem 40000 euros bruts anuals, haurem de pagar:
el 19% dels primers 12450€ (0,19* 12450)
més el 24% dels (20199-12450)€ ( 0,24*( 20199-12450))
més el 30% dels (35199 - 20199)€ ( 0,3*( 35199 - 20199))
més el 37% dels (40000 - 20199)€ ( 0,37*( 40000 - 20199))
"""

def pagament_irpf(brut,trams):
    try:
        if type(trams) != dict:
            raise NameError("the second argument must be a dictionary")
    except NameError as e:
        return e
    
    try:
        if not brut == int(brut):
            raise TypeError("the first argument must be a integer")
    except TypeError as e:
        return e

    try:
        lista_keys = list(trams.keys())
        for i in lista_keys:
            if not i == int(i):
                raise ValueError("There is a key that is not a integer")
    except ValueError as e:
        return e
    
    try:
        for i in trams:
            if trams[i] == int(trams[i]):
                raise ValueError("There is a value that is not a integer")
    except ValueError as e:
        return e

trams = {12450:19,299999:45,35199:30,59999:37,20199:24,300000:47}




def exercici2(cadena,exceptions):

    try:
        if type(cadena) != str:
            raise ValueError("The options have to be a string")
        
    except ValueError as e:
        
        return e

    try:
        if type(exceptions) != tuple:
            raise ZeroDivisionError("The exceptions have to be a tuple")
        
    except ZeroDivisionError as e:
        
        return e
    
    try:
        total_opciones = cadena.count(";")
        if total_opciones < 2:
            raise FileNotFoundError("The minimun length of the options are 2")
        
    except FileNotFoundError as e:
        
        return e
    
    
    total_opciones = cadena.count(";")
    while True:
        for i in range(total_opciones):
            if i == 0:
                inicio = 0
                final = cadena.find(";")
                opcion_iesima = cadena[inicio:final]
                print("{}) {}".format(i + 1,opcion_iesima))

            else:
                inicio = final + 1
                final = cadena.find(";", inicio)
                opcion_iesima = cadena[inicio:final]
                print("{}) {}".format(i + 1,opcion_iesima))
            
        opcion = input("Opcion: ")
        try:
            if not opcion.isdigit() and not opcion in exceptions:
                
                raise TypeError("The option is not a number and is not in exceptions")
            if opcion.isdigit() and not opcion in exceptions:
                
                opcion = int(opcion)
                
                if opcion not in range(1, total_opciones + 1) and not opcion in exceptions:
                    
                    raise TypeError("The option is out of range and not in exceptions")
            if opcion:
                return opcion
            
        except TypeError as e:
            print(e)
            input("Enter to continue")

cadena = "opcio1;opcio2;opcio3;"
cadena2 = ["Opcio1","Opcio2","Opcio3"]
print(exercici2(cadena,exceptions=("c","d", 10, "11")))








def imprimeix_productes(n):
    resultado = 0
    if n <= 1:
        return resultado
    else:
        resultado = imprimeix_productes(n-1)

    print("{}*{}*{} = {}".format(n-2,n-1,n,(n-2)*(n-1)*(n)))
    return resultado

imprimeix_productes(6)



def caracters_iguals(string1,string2):

    resultado = ""
    
    if len(string1) == 0:
        return resultado
    
    if string1[0] in string2:
        
        resultado += string1[0] + caracters_iguals(string1.replace(string1[0],"")[1:],string2)
    else:
        resultado += caracters_iguals(string1[1:],string2)
    
    return resultado

print(caracters_iguals("abccddd","ccddeeeef"))