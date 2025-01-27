
letrasDni = ['T','R','W','A','G','M','Y','F','P','D','X','B','N','J','Z','S','Q','V','H','L','C','K','E']
usuario1 = {"nombre":"Pedro Javier Morales",  "direccion": "Flores 36 8º 2º", "tfn":["+0034345345345"],"compras":[1234,423,23]}
usuario2 = {"nombre":"Maite Lopez Miravet", "direccion":"Balmes 31 1º 2º","tfn":["+0034234234235","+0034239999235"],"compras":[12344]}
usuario3 = {"nombre":"Marta Garcia Suarez",  "direccion":"Valencia 21 3º 1º","tfn": ["+0075766576575"],"compras":[34,423,23,6]}
usuarios = {"47474747X":usuario1,"24536425T":usuario2,"76767676H":usuario3}

salir = False
flg_01 = False
flg_02 = False
flg_03 = False
flg_04 = False
flg_05 = False

menu00 = "1)Create User\n2)Modify user\n3)Show Users\n4)Find Users\n5)List Users\n6)Exit"
menu01 = "1)Enter Dni\n2)Enter Name\n3)Enter Surname\n4)Enter Address\n5)Enter Tfn\n6)Save User\n7)Go Back"
menu02 = "\n"+"Menu 02 - Modify User".center(50,"*")+"\n"+"1)Add purchase\n2)Add tfn number\n3)Del tfn number\n4)Change address\n5)Go Back"
menu05 = "1)List Users by DNI\n2)List Users by Name\n3)List Users by Address\n4)List Users by Total Purchase\n5)Go back"
menu04 = "1)Find Users by DNI\n2)Find Users by Name\n3)Go back"

while not salir:
    print(menu00)
    opc = input("Opcion: ")
    if opc == 1:
        flg_01 = True
        salir = True




while flg_01:
    print(menu01)