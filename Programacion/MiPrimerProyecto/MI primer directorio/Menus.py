# menu0 = "Menu0".center(50,"*") + "\n" + "\n"
# menu01 = "Menu01".center(50,"*") + "\n" + "\n"
# menu02 = "Menu02".center(50,"*") + "\n" + "\n"
#
# menu011 = "Menu011".center(50,"*") + "\n" + "\n"
# menu012 = "Menu012".center(50,"*") + "\n" + "\n"
#
# menu021 = "Menu021".center(50,"*") + "\n" + "\n"
# menu022 = "Menu022".center(50,"*") + "\n" + "\n"
#
# menu0 = menu0 + "1) Menu01 \n2) Menu02\n3) Salir"
# menu01= menu01 + "1) Menu011 \n2) Menu012\n3) Atras"
# menu02= menu02 + "1) Menu021 \n2) Menu022\n3) Atras"
#
# menu011= menu011 + "1) Menu0111 \n2) Menu0112\n3) Atras"
# menu012= menu012 + "1) Menu0121 \n2) Menu0122\n3) Atras"
#
# menu021= menu021 + "1) Menu0211 \n2) Menu0212\n3) Atras"
# menu022= menu022 + "1) Menu0221 \n2) Menu0222\n3) Atras"
#
#
# salir = False
# print(menu0)
# while not salir:
#     opcion = int(input("Opcion: "))
#     if opcion == 1:
#         print(menu01)
#         while not salir:
#             opcion = int(input("Opcion: "))
#             if opcion == 1:
#                 print(menu011)
#             elif opcion == 2:
#                 print(menu012)
#             elif opcion == 3:
#                 print(menu0)
#             else:
#                 print("Opcion invalida (Marca un numero de las opciones)")
#     elif opcion == 2:
#         print(menu02)
#         while not salir:
#             opcion = int(input("Opcion: "))
#             if opcion == 1:
#                 print(menu021)
#             elif opcion == 2:
#                 print(menu022)
#             elif opcion == 3:
#                 print(menu0)
#             else:
#                 print("Opcion invalida (Marca un numero de las opciones)")
#     elif opcion == 3:
#         salir = True
#     else:
#         print("Opcion invalida (Marca un numero de las opciones)")
"""
Es mejor hacerlo con flg_00 = False o true esto para cada uno de los menus asi es mas sencillo y cuando queramos pasar de un menu a otro solo consta
de pasar una de las variabes de true a false y viceversa
"""

