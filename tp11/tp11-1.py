def cargar(lista = []):
  entrada = ""
  while(entrada.lower() != "salir"):
    entrada = input("Ingrese un numero\n> ")
    if(entrada.lower() != "salir"):
      lista.append(entrada)



def main():
  lista = [1,43,35]
  cargar(lista)
  print(lista)

main()