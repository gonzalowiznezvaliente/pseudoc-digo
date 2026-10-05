def clasificar_imc(peso, altura):
    imc = peso / (altura ** 2)
    if imc < 18.5:
        return imc, "Bajo peso"
    if imc < 25:
        return imc, "Normal"
    return imc, "Sobrepeso"



peso = float(input("Peso en kg: "))
altura = float(input("Altura en metros: "))


imc, categoria = clasificar_imc(peso, altura)
print(f"\nIMC: {imc:.2f} | Clasificación: {categoria}")