def tabletsBarats(nomf1, nomf2, p):
    try:
        f_in = open(nomf1, 'r')
        f_out = open(nomf2, 'w')
        for linea in f_in:
            parts = linea.split(';')
            if len(parts) < 5:
                continue
            
            marca = parts[0]
            model = parts[1]
            cpu = parts[2]
            velocitat = int(parts[3])
            preu = float(parts[4])

            if preu < p:
                nom_model = marca[:3].upper() + "-" + model

                if velocitat < 500:
                    nivell_velocitat = "Baixa"
                elif 500 <= velocitat <= 900:
                    nivell_velocitat = "Mitjana"
                else:
                    nivell_velocitat = "Alta"

                f_out.write(nom_model + " " + nivell_velocitat + "\n")

        print("Fitxer '" + nomf2 + "' creat correctament.")
        print("\n📂 Contingut del fitxer '" + nomf2 + "':\n")

        f_out = open(nomf2, 'r')
        for linea in f_out:
            print(linea, end="")
    except Exception as e:
        print("Error:", e)

tabletsBarats('tablets.txt', 'barats.txt', 100)

