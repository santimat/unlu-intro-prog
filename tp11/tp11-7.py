def buscar(lista_personas, busqueda):
  personas_encontradas = []
  largo_busqueda = len(busqueda)
  i = 0
  for persona in lista_personas:
    largo_persona = len(persona)
    coincide = False
    i = 0
    # importante restar para que el largo del término de busqueda entre en la busqueda, sino estaríamos intentando acceder a indices no existentes
    stop = largo_persona - largo_busqueda
    while i <= stop and not coincide:
      j = 0
      coinciden_letras = True
      while (j < largo_busqueda):
        if(persona[j].lower() != busqueda[j].lower()):
          coinciden_letras = False
        j = j + 1

      if(coinciden_letras):
        coincide = True
      
      i = i + 1

    if(coincide):
      personas_encontradas.append(persona)
  return personas_encontradas  


def main():
  lista_personas = [
    "Juan Carlos",
    "María Belén",
    "Lucas Agustín",
    "Ana Clara",
    "Mariano",
    "Santiago",
    "santino",
    "sara",
    "Facundo",
    "Giuliana"]
  busqueda = "sa"

  encontradas = buscar(lista_personas, busqueda)
  print(encontradas)
main()