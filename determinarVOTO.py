def verificar_puede_votar(edad, nacionalidad):
    # Usamos .lower() para que acepte "Española", "ESPAÑOLA" o "española"
    if edad >= 18 and nacionalidad.lower() == "española":
        puede_votar = True
    else:
        puede_votar = False
        
    return puede_votar


# --- LLAMADAS DE PRUEBA ---

print(verificar_puede_votar(20, "española"))   # Devuelve: True
print(verificar_puede_votar(16, "española"))   # Devuelve: False
print(verificar_puede_votar(25, "italiana"))   # Devuelve: False
print(verificar_puede_votar(15, "francesa"))   # Devuelve: False
print(verificar_puede_votar(65, "Española"))   # Devuelve: True