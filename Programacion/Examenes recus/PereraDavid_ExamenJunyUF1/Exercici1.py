"""
Exercici 1:
Crearem una aplicació que ens servirà per gestionar les nostres tasques anuals.
Utilitzarem el següent string per emmagatzemar les tasques, cada tasca tindrà el dia com l'any com
el mes com la tasca en si.
tasks = "2025#April#12#Anar al metge***2025#April#3#Revisió
ITV***2025#June#10#Estudiar per l'examen de M3***2025#June#14#Declaracio
hisenda***2025#September#11#Pagament Matricula***"
Cada tasca està separada per “***”
Totes les tasques estan ordenades de major a menor prenent com a referència primer l'any després el
mes i després el dia.
Necessitarem tambè la següent llista i el següent diccionari:
days_per_month =
{"January":31,"February":29,"March":31,"April":30,"May":31,"June":30,"July":31,"Au
gust:31":31,"September":30,"October":31,"November":30,"December":31}
months =
["January","February","March","April","May","June","July","August","September","Oc
tober","November","December"]
Veiem que el diccionari days_per_month ens serveix per saber quants dies té cada mes durant l'any.
La llista months conté els mesos ordenats.
L'aplicació començarà amb el menú següent:
Com a tot menú, haurem de comprovar que no s'introdueix una opció no numèrica i que tampoc no
s'introdueix una opció numèrica fora del rang correcte.
En cas d'introduir un caràcter no numèric se'ns mostrarà el missatge següent:
"Not numeric option"
En cas d'introduir un número fora del rang es mostrarà el missatge següent:
"Option out of range"
L'opció 1 ens mostrarà la taula següent:
L'opció 2 ens servirà per introduir una nova tasca, i ens mostrarà el menú següent:
En cas d'introduir un caràcter no numèric se'ns mostrarà el missatge següent:
"Not numeric option"
En cas d'introduir un número fora del rang es mostrarà el missatge següent:
"Option out of range"
Si intenteu introduir el dia abans del mes, es mostrarà el següent missatge.
"First enter the moth"
El mes s'inserirà en format numèric 1-12.
Si introduïm un mes fora del rang 1 a 12, es mostrarà el missatge següent:
"Invalid month"
i se'ns tornarà a demanar el mes.
Si inserim un caràcter no numèric al mes, se'ns mostrarà el missatge següent:
"Not numeric month"
i se'ns tornarà a demanar el mes.
Un cop hàgim introduït el mes, podrem introduir el dia.
Si inserim un caràcter no numèric al dia, se'ns mostrarà el missatge següent:
"Not numeric day"
i se'ns tornarà a demanar el dia.
Si introduïm un dia fora del rang 1 al dia que tenim al diccionari days_per_month, se'ns mostrarà el
missatge següent:
"Invalid day for the month "Abril
i se'ns tornarà a demanar el dia.
L'any haurà de ser més gran que 2000.
Si inserim un caràcter no numèric a l'any, se'ns mostrarà el missatge següent:
"Not numeric year"
i se'ns tornarà a demanar el dia.
Si introduïm un any menor o igual al 2000, se'ns mostrarà el missatge següent:
"Invalid year"
i ens tornarà a demanar l'any.
La tasca haurà de ser un text no buit.
En cas d'intruduir una tasca buida, ens mostrarà el missatge següent:
"Invalid task"
i ens tornarà a demanar la tasca.
Un cop hàgim introduït tant el dia com el mes com l'any com la pròpia tasca ja podrem enregistrar
la tasca.
En cas que escollim enregistrar la tasca i no hàgim introduït el dia se'ns mostrarà el següent
missatge:
"Enter the day of the task"
En cas que escollim enregistrar la tasca i no hàgim introduït el mes ens mostrarà el següent
missatge:
"Enter the month of the task"
En cas que escollim enregistrar la tasca no hàgim introduït l'any ens mostrarà el missatge següent:
"Enter the year of the task"
En cas que escollim enregistrar la tasca i no hàgim introduït la pròpia tasca ens mostrarà el missatge
següent:
"Enter the task"
En cas que ja hàgim introduït totes les dades es gravarà la tasca al nostre string de manera que quedi
ordenat de major a menor primer per any, després per mes, i després per dia.
Puntuació:
Menu totalment funcional→ 1 punt
Mostrar taula amb tascas → 2 punts.
Enregistrar nova tasca ordenada → 2 punts
L'ús del mètode .split() invalidarà tot l'exercici
"""

salir = True
flag_00 = True
flag_01 = False
flag_02 = False


tasks = "2025#April#12#Anar al metge***2025#April#3#RevisióITV***2025#June#10#Estudiar per l'examen de M3***2025#June#14#Declaracio hisenda***2025#September#11#Pagament Matricula***"

days_per_month = {"January":31,"February":29,"March":31,"April":30,"May":31,"June":30,"July":31,"August:31":31,"September":30,"October":31,"November":30,"December":31}
months = ["January","February","March","April","May","June","July","August","September","October","November","December"]

menu00 = "Exercici1" + "\n" + "1) Show Tasks" + "\n" + "2) New Task" + "\n" + "3) Exit"
menu02 = "1) Day of the new task" + "\n" + "2) Month of the new task" + "\n" + "3) Year of the new task" + "\n" + "4) New task" + "\n" + "5) Save task" + "\n" + "6) Back"



while salir:
    while flag_00:
        print(menu00)
        opcion = input("Option: ")
        if not opcion.isdigit():
            print("Not numeric option")
        else:
            opcion = int(opcion)
            if not opcion in range(1, 4):
                print("Option out of range")
            else:
                if opcion == 1:
                    flag_01 = True
                    flag_00 = False
                if opcion == 2:
                    flag_02 = True
                    flag_00 = False
                if opcion == 3:
                    salir = False
                    flag_00 = False
                    print("Exiting...")
    
    while flag_01:
        total_jugadores = tasks.count("***")
        datos = ""
        for i in range(total_jugadores):
            if i == 0:
                inicio = 0
                final = tasks.find("***")
                task_iesima = tasks[inicio:final]

            else:
                inicio = final + 3
                final = tasks.find("***", inicio)
                task_iesima = tasks[inicio:final]
            
            # jugadores = "LeBron James,30:90,206;113-Stephen Curry,28:95,191;86-Kobe Bryant,29:85,198;96"

            asterisco1 = task_iesima.find("#")
            asterisco2 = task_iesima.find("#", asterisco1)
            asterisco3 = task_iesima.find("#", asterisco2)
            
            año = task_iesima[:asterisco1]
            mes = task_iesima[asterisco1 + 1:asterisco2]
            dia = task_iesima[asterisco2 + 1:asterisco3]
            task = task_iesima[asterisco3+1:]
            
            
            datos+= str(año).ljust(35) + mes.ljust(10) + str(dia).rjust(10) + task.rjust(30)
            print(datos)

        
            


    new_day = ""
    new_month = ""
    new_year = ""
    new_task = ""
    while flag_02:
        print(menu02)
        opcion = input("Option: ")
        if not opcion.isdigit():
            print("Not numeric option")
        else:
            opcion = int(opcion)
            if not opcion in range(1, 7):
                print("Option out of range")
            else:
                if opcion == 1:
                    if new_month == "":
                        print("First enter the moth")
                    else:
                        while True:
                            new_day = input("Introduce new day: ")
                            if not new_day.isdigit():
                                print("Not numeric day")
                            else:
                                new_day = int(new_day)
                                if new_day not in range (1,days_per_month[new_month]+1):
                                    print("Invalid day for the month {}".format(new_month))
                                else:
                                    break

                if opcion == 2:
                    while True:
                        new_month = input("Introduce new month: (1-12) ")
                        new_month = int(new_month)
                        if new_month not in range(1,13):
                            print("Invalid month")
                        else:
                            new_month = months[new_month-1]
                            print(new_month)
                            break

                if opcion == 3:
                    while True:
                        new_year = input("Introduce a new year: ")
                        if not new_year.isdigit():
                            print("Not numeric year")

                        else:
                            new_year = int(new_year)
                            if new_year <= 2000:
                                print("Invalid year")
                            else:
                                break

                if opcion == 4:
                    while True:
                        new_task = input("INtroduce your task: ")
                        if new_task == "":
                            print("Invalid task")
                        else:
                            break

                if opcion == 5:
                    if new_day == "":
                        print("Enter the day of the task")
                    if new_month == "":
                        print("Enter the month of the task")
                    if new_year == "":
                        print("Enter the year of the task")
                    if new_task == "":
                        print("Enter the task")
                    else:
                        task = "{}#{}#{}#{}***".format(new_year,new_month,new_day,new_task)
                        total_tasks = tasks.count("***")
                        for i in range(total_tasks):
                            task_iesima = tasks
                            if i == 0:
                                inicio = 0
                                final = tasks.find("***")
                                task_iesima = tasks[inicio:final]
                            else:
                                inicio = final + 3
                                final = tasks.find("***",inicio)

                            asterisco1 = tasks.find("#")
                            asterisco2 = tasks.find("#")
                            asterisco3 = tasks.find("#",asterisco2)

                            nombre_disco = task_iesima[:asterisco1]
                            ano = task_iesima[asterisco1+1:task_iesima.find("#")]
                            grupo = task_iesima[asterisco2+1:asterisco3]
                            
                            

                            
                            
                            
                    



                if opcion == 6:
                    salir = False
                    print("Exiting...")



    while flag_01:
        continue