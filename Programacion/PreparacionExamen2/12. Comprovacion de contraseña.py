# Crear un programa per validació de contrasenyes. Aquest programa,
# haurà de complir amb els següents criteris d'acceptació:
# contrasenya ha de tenir un mínim de 8 caràcters.
# contenir lletres minúscules, majúscules, números i  1 caràcter no alfanumèric.
# La contrasenya no pot contenir espais en blanc
# Contrasenya vàlida, retorna True
# Contrasenya no vàlida, retorna el missatge
# "La contrasenya triada no és segura".

# Pedimos contraseña
contrasenya = input("Introdueix la teva contrasenya: ")

# condiciones #

minim_longitud = len(contrasenya) >= 8
te_minuscula = False
te_majuscula = False
te_numero = False
te_no_alfanumeric = False
sense_espais = True

# Recorremos cada carácter de la contraseña para verificar las condiciones
# isdigit(): Compruba que contiene solo números.
# isalpha(): Compruba que contiene solo letras.
# isalnum(): compruba que contiene solo letras y números sin espacios ni otros caracteres.
# islower(): compruba que contiene minúsculas(True)
# (false) si contiene mayusculas,números o caracteres especiales
# isupper() compruba que contiene mayusculas (True)
# (false) si contiene minusculas,números o caracteres especiales
# not .isalnum(): contiene caracteres no enpeciales (no alfanumericos) (como @, #, etc.).
# j.isspace():  # contiene un espacio (true)
for j in contrasenya:
    if j.islower():
        te_minuscula = True
    if j.isupper():
        te_majuscula = True
    if j.isdigit():
        te_numero = True
    if not j.isalnum():
        te_no_alfanumeric = True
    if j.isspace():
        sense_espais = False #ponemos False si hay un espacio
#ponemos if para verificar que se cumplen todas las condiciones
# Verificamos si la contraseña cumple todas las condiciones
if (minim_longitud and te_minuscula and te_majuscula and te_numero
        and te_no_alfanumeric and sense_espais):
    print(True)
else:
    print("La contrasenya triada no és segura")
