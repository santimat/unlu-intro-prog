def mostrar_dos_primeros_caracteres(palabra = ""):
  caracteres = "" 
  for letra in range(2):
    caracteres = caracteres + palabra[letra]
  
  print(f"Los dos primeros caracteres de {palabra} son {caracteres}")

def mostrar_tres_ultimos_caracteres(palabra = ""):
  if len(palabra) < 3: 
    print("Palabra muy corta")
  else:
    caracteres = ""
    largo_palabra = len(palabra)
    for letra in range(largo_palabra -3, largo_palabra):
      caracteres = caracteres + palabra[letra]
    print(f"Los ultimos tres caracteres de {palabra} son {caracteres}")
    

def mostrar_invertido(palabra = ""):
  palabra_invertida = ""
  for letra in range(len(palabra) - 1, -1, -1):
    palabra_invertida = palabra_invertida + palabra[letra]

  print(f"{palabra} invertida:")
  print(palabra_invertida)

def main():
  mostrar_dos_primeros_caracteres("pepe")
  mostrar_tres_ultimos_caracteres("santino")
  mostrar_invertido("epep")

main()