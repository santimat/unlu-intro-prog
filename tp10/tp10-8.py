def obtener_palabra():
  palabra = input("Ingrese una palabra\n>")
  return palabra


def obtener_consonantes(palabra = ""):
  consonantes = ""
  for indice in range(len(palabra)):
    palabra_actual = palabra[indice].lower()

    if(palabra_actual != "a" 
       and palabra_actual != "e" 
       and palabra_actual != "i" 
       and palabra_actual != "u" 
       and palabra_actual != "o"):
      consonantes = consonantes + palabra_actual

  return consonantes


def main():
  palabra = obtener_palabra()
  consonantes = obtener_consonantes(palabra)
  print(f"Las consonantes en la palabra: {palabra} son: {consonantes}")

main()