def pedir_palabra():
  palabra = input("Ingrese una palabra que contenga ñ\n> ")
  tiene_enie = False
  i = 0
  while palabra == "" or not tiene_enie:
    while(i < len(palabra) and not tiene_enie):
      if palabra[i].lower() == "ñ":
        tiene_enie = True
      i = i + 1

    if not tiene_enie:
      palabra = input("Ingrese una palabra valida\n> ")
      i = 0

  return palabra

def transformar_palabra(palabra):
  nueva_palabra = ""
  for letra in palabra:
    if(letra.lower() == "Ñ"):
      nueva_palabra = nueva_palabra + "n"
    else: 
      nueva_palabra = nueva_palabra + letra
  return nueva_palabra.upper()

      

def main():
  palabra = pedir_palabra()
  print(f"{palabra} tiene {len(palabra)} letras")
  palabra_cambiada = transformar_palabra(palabra)
  print(f"La palabra cambiada queda así: {palabra_cambiada}")

main()