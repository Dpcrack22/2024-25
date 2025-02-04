menu00 = True
menu01 = False
menu02 = False
menu011 = False
menu012 = False
menu021 = False
menu022 = False
menu0221 = False
menu0222 = False

while True:
    if menu00:
        print("Menú 00:")
        print("1) Menú 01")
        print("2) Menú 02")
        print("3) Sortir")
        opcio = input("Selecciona una opció: ")

        if opcio == "1":
            menu00 = False
            menu01 = True
        elif opcio == "2":
            menu00 = False
            menu02 = True
        elif opcio == "3":
            break
        else:
            print("Opció no vàlida. Torna a intentar-ho.")

    elif menu01:
        print("Menú 01:")
        print("1) Menú 011")
        print("2) Menú 012")
        print("3) Tornar enrere")
        opcio01 = input("Selecciona una opció: ")

        if opcio01 == "1":
            menu01 = False
            menu011 = True
        elif opcio01 == "2":
            menu01 = False
            menu012 = True
        elif opcio01 == "3":
            menu01 = False
            menu00 = True
        else:
            print("Opció no vàlida. Torna a intentar-ho.")

    elif menu02:
        print("Menú 02:")
        print("1) Menú 021")
        print("2) Menú 022")
        print("3) Tornar enrere")
        opcio02 = input("Selecciona una opció: ")

        if opcio02 == "1":
            menu02 = False
            menu021 = True
        elif opcio02 == "2":
            menu02 = False
            menu022 = True
        elif opcio02 == "3":
            menu02 = False
            menu00 = True
        else:
            print("Opció no vàlida. Torna a intentar-ho.")

    elif menu011:
        print("Menú 011:")
        print("1) Opción 1 del Menú 011")
        print("2) Opción 2 del Menú 011")
        print("3) Tornar enrere")
        opcio011 = input("Selecciona una opció: ")

        if opcio011 == "1":
            print("Has triat el Menú 0111.")
        elif opcio011 == "2":
            print("Has triat el Menú 0112.")
        elif opcio011 == "3":
            menu011 = False
            menu01 = True
        else:
            print("Opció no vàlida. Torna a intentar-ho.")

    elif menu012:
        print("Menú 012:")
        print("1) Opción 1 del Menú 012")
        print("2) Opción 2 del Menú 012")
        print("3) Tornar enrere")
        opcio012 = input("Selecciona una opció: ")

        if opcio012 == "1":
            print("Has triat el Menú 0121.")
        elif opcio012 == "2":
            print("Has triat el Menú 0122.")
        elif opcio012 == "3":
            menu012 = False
            menu01 = True
        else:
            print("Opció no vàlida. Torna a intentar-ho.")

    elif menu021:
        print("Menú 021:")
        print("1) Opción 1 del Menú 021")
        print("2) Opción 2 del Menú 021")
        print("3) Tornar enrere")
        opcio021 = input("Selecciona una opció: ")

        if opcio021 == "1":
            print("Has triat el Menú 0211.")
        elif opcio021 == "2":
            print("Has triat el Menú 0212.")
        elif opcio021 == "3":
            menu021 = False
            menu02 = True
        else:
            print("Opció no vàlida. Torna a intentar-ho.")

    elif menu022:
        print("Menú 022:")
        print("1) Menú 0221")
        print("2) Menú 0222")
        print("3) Tornar enrere")
        opcio022 = input("Selecciona una opció: ")

        if opcio022 == "1":
            menu022 = False
            menu0221 = True
        elif opcio022 == "2":
            menu022 = False
            menu0222 = True
        elif opcio022 == "3":
            menu022 = False
            menu02 = True
        else:
            print("Opció no vàlida. Torna a intentar-ho.")

    elif menu0221:
        print("Menú 0221:")
        print("1) Opción 1 del Menú 0221")
        print("2) Tornar enrere")
        opcio0221 = input("Selecciona una opció: ")

        if opcio0221 == "1":
            print("Has triat el Menú 0221.1.")
        elif opcio0221 == "2":
            menu0221 = False
            menu022 = True
        else:
            print("Opció no vàlida. Torna a intentar-ho.")

    elif menu0222:
        print("Menú 0222:")
        print("1) Opción 1 del Menú 0222")
        print("2) Tornar enrere")
        opcio0222 = input("Selecciona una opció: ")

        if opcio0222 == "1":
            print("Has triat el Menú 0222.1.")
        elif opcio0222 == "2":
            menu0222 = False
            menu022 = True
        else:
            print("Opció no vàlida. Torna a intentar-ho.")
