def invertir_lista(lista_palabras): 
  lista_invertida = []
  for palabra in range(len(lista_palabras) - 1, -1, -1):
    lista_invertida.append(lista_palabras[palabra])

  return lista_invertida


def main():
  palabras = ["dia","buen","messi","leo"]
  lista_invertida = invertir_lista(palabras)
  print(palabras)
  print("-----------------")
  print(lista_invertida)

main()