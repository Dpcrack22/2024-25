import os.path
#usamos el import os.pat para importar la raiz del archivo
# luego usaos el open para abrir dicho archivo almacenandolo en ua variable, eso si, deberemos de usar el .close al final para cerrarlo
# sino será un 0 en el examen
# si usamos el open a secas, podeos usar el write, read, etc siempr eque el archivo haya sido creado exteriormente
# si el archivo no lo hemos creado, simplemente deberemos de usr el open("nombre","w") para que el archivo se cree automáticamente

ficherob=open("ejemplofichero2","w")
# para leer el archivo, lo introducimos en una variable, y este nos cogerá los bits que haya en las lineas
leemamon=ficherob.read()
print(leemamon)
# podemos mediante un for, iterar sobe las lineas y que este nos imprima cada linea que haya en el archivo txt
ficherob.close()