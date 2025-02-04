if not choice.isdigit():
    print("Only numerical option")
    input("Retry: ")

else:
    choice = int(choice)
    if choice not in range(1, 4):
        print("Not in range option")
        input("Press Enter to ")

auxiliar_id = auxiliar[i][0]
auxiliar_nombre = auxiliar[i][1]["name"]
auxiliar_speed = auxiliar[i][1]["speed"]
auxiliar_strength = auxiliar[i][1]["strength"]
auxiliar_exp = auxiliar[i][1]["experience"]