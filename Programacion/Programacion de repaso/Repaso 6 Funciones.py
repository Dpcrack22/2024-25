#Cuidado con el hecho de decir "hazme una funcion que devuelva sera return" si dice "Hacme una funcion que imprima sera print"



def funcion(a):
    print("Funcion")
    return "Lo que sea"
    return str(a)

funcion("aaa")
print(funcion(""))


def notas_RAs(Notas_UFs):
    notas_ras = (notas_ufs[0],notas_ufs[3],0.5*notas_ufs[0]+0.25*notas_ufs[1]+0.25*notas_ufs[5],0.4*notas_ufs[1]+0.6*notas_ufs[3],0.4*notas_ufs[2]+0.6*notas_ufs[5],notas_ufs[0],notas_ufs[3],notas_ufs[4],notas_ufs[4])
 
    cabecera = ""
    for i in range(9):
        cabecera += "Nota RA" + str(i+1).rjust(10)
    
    print(cabecera)
    
    datos = ""
    for nota in notas_ras:
        datos += str(nota).rjust(10)
    print(datos)
 
    return notas_ras


notas_ufs = (1.50,1.75,6.00,9.00,6.00,10.00)
print(notas_RAs(notas_ufs))

