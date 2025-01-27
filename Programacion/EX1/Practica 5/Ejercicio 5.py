HoresSetmanals = float(input("Donam el numero d'hores setmanals: "))
PreuHora = float(input("Donam el preu pero hora: "))
ImportTotal = 0.0

if HoresSetmanals <= 35:
    ImportTotal = HoresSetmanals * PreuHora
else:
    HoresNormals = 35
    HoresExtra = HoresSetmanals - HoresNormals
    ImportTotal = (HoresNormals * PreuHora) + ( HoresExtra * PreuHora * 1.5)

print("L'import total del treballador es {:.2f} euros ".format(ImportTotal))