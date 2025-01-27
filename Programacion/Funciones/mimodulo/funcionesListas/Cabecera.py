#
# def cabecera(titulo, *submenu):
#     if len(submenu) == 1:
#         col1 = submenu[0]
#         submenu_procesado = [col1]
#         print(submenu_procesado)
#     elif len(submenu) == 2:
#         col1 = submenu[0]
#         col2 = submenu[1]
#         submenu_procesado = [col1, col2 ]
#         print(submenu_procesado)
#     elif len(submenu) == 3:
#         col1 = submenu[0]
#         col2 = submenu[1]
#         col3 = submenu[2]
#         submenu_procesado = [col1, col2 ,col3]
#         print(submenu_procesado)
#     elif len(submenu) == 4:
#         col1 = submenu[0]
#         col2 = submenu[1]
#         col3 = submenu[2]
#         col4 = submenu[3]
#         submenu_procesado = [col1, col2 ,col3 , col4]
#
#         print(submenu_procesado)
#
#     elif len(submenu) == 5:
#         col1 = submenu[0]
#         col2 = submenu[1]
#         col3 = submenu[2]
#         col4 = submenu[3]
#         col5 = submenu[4]
#         submenu_procesado = [col1, col2 ,col3 , col4 , col5]
#         for i in submenu_procesado:
#             print(i)
#         print(submenu_procesado)

#     #submenu_procesado = col1.
#     #menu = "-"*50 + "\n" + titulo.center(50) + "\n" + submenu_procesado + "\n" + "-"*50
#     #print(menu)
#
# cabecera("Lista Contactos", "DNI","Nombre","Telefono","Puntos","Dados")

columnas = [{"name":"columna1","alineacion":"l","espaciado":10},
                       {"name":"columna2","alineacion":"r","espaciado":15},
                       {"name":"columna3","alineacion":"l","espaciado":20},
                       {"name":"columna4","alineacion":"r","espaciado":10}]

def funcion_cabeceras(columnas,titulo="",relleno="*"):
    long = 0
    for columna in columnas:
        long += columna["espaciado"]
    long = long + len(columnas)-1
    cabecera = titulo.center(long, relleno)+"\n"
    for columna in columnas:
        if columna["alineacion"] == "l":
            cabecera += columna["name"].ljust(columna["espaciado"])
        else:
            cabecera += columna["name"].rjust(columna["espaciado"])
        cabecera += " "
    cabecera= cabecera[:-1]
    cabecera += "\n"
    cabecera += relleno*long
    cabecera += "\n"
    print(cabecera)

funcion_cabeceras(columnas,titulo="Peter")