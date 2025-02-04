def imprimir_menu():
    # Menú como string
    menu_str = "1) Opción 1; 2) Opción 2; 3) Opción 3"
    print("Menú con String:")
    opciones_str = menu_str.split(";")
    for opcion in opciones_str:
        print(opcion.strip())
    print()  # Salto de línea
    
    # Menú como lista
    menu_lista = ["Opción 1", "Opción 2", "Opción 3"]
    print("Menú con Lista:")
    for i, opcion in enumerate(menu_lista, start=1):
        print(f"{i}) {opcion}")
    print()  # Salto de línea
    
    # Menú como diccionario
    menu_dict = {1: "Opción 1", 2: "Opción 2", 3: "Opción 3"}
    print("Menú con Diccionario:")
    for clave, valor in menu_dict.items():
        print(f"{clave}) {valor}")
    
# Llamar a la función para ver los resultados


personas = {
    "12345678A": {
        "nombre": "Juan",
        "apellidos": "Pérez García",
        "telefono": "123456789",
        "direccion": "Calle Falsa 123"
    },
    "23456789B": {
        "nombre": "Ana",
        "apellidos": "Martín López",
        "telefono": "987654321",
        "direccion": "Avenida Siempre Viva 456"
    },
    "34567890C": {
        "nombre": "Carlos",
        "apellidos": "González Sánchez",
        "telefono": "555555555",
        "direccion": "Calle del Sol 789"
    }
}

def añadir_user(diccionario):

    DNI = input("Dame tu dni: ")
    NAME = input("Dame tu nombre: ")
    APELLIDOS = input("Dime tus apellidos: ")
    TFN = input("Dime tus telefono: ")
    DIRECCION = input("Dime tus direccion: ")

    nuevo_usuario = {
        "nombre":NAME,
        "apellidos":APELLIDOS,
        "telefono":TFN,
        "direccion":DIRECCION
    }

    diccionario[DNI] = nuevo_usuario
    print(diccionario)



def listar_diccionario(diccionario,campo):
    claves = list(diccionario.keys())
    n = len(claves)
    

listar_diccionario(personas,"nombre")
    

    