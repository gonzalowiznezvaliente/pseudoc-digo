def clasificar_nota(nota):
    if nota < 0 or nota > 10:
        return "Nota no válida (debe ser entre 0 y 10)"
    if nota < 5:
        return "Insuficiente"
    if nota < 7:
        return "Suficiente"
    if nota < 9:
        return "Notable"
    return "Sobresaliente"


nota_examen = float(input("Introduce la nota de tu examen (ej. 7.5): "))

resultado = clasificar_nota(nota_examen)

print(f"\nNota introducida: {nota_examen} | Resultado: {resultado}")