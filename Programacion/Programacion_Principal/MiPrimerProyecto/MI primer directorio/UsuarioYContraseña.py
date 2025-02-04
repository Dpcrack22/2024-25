
Usuario_Correcto = True
Contrasena_Correcto = True
#
# while Usuario_Correcto:
#     usuario = input("Pon un usuario")
#     if not usuario.isalnum():
#         print("El nom d'usuari pot contenir només lletres i números")
#     elif len(usuario) <6:
#         print("El nom de usuari ha de contenir almenys 6 caràcters")
#     elif len(usuario) >12:
#         print("El nom de usuari no pot contenir més de 12 caràcters")
#     else:
#         print("Usuari Correcte")
#         input("Enter to continue: ")
#         Contrasena_Correcto = True
#         Usuario_Correcto = False

while Contrasena_Correcto:
    Contrasena = input("Pon una Contraseña")
    if len(Contrasena) < 8:
        print("La contrasenya ha de contenir almenys 8 caràcters")
    elif Contrasena.islower() and not Contrasena.isalnum() >1:
        print("guay")


    else:
        print("Usuari Correcte")
        input("Enter to continue: ")