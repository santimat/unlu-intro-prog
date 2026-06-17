def obtener_primos(lista_numeros):
  numeros_primos = []
  for numero in lista_numeros:
    es_primo = True

    for n in range(2,numero):
      if(numero % n == 0):
         es_primo = False

    if(es_primo):
      numeros_primos.append(numero)

  return numeros_primos

def obtener_sumatoria_promedio(lista_numeros):
  sumatoria = 0
  for numero in lista_numeros:
    sumatoria = sumatoria + numero

  promedio = sumatoria / len(lista_numeros)

  return sumatoria,promedio

def mostrar_factorial(lista_numeros):
  for numero in lista_numeros:
    factorial = 1
    for n in range(1, numero + 1):
      factorial = factorial * n
    print(f"El factorial !{numero} es: {factorial}")


def main():
  lista_numeros= [5,7,14,13,3,1,15,17]
  numeros_primos = obtener_primos(lista_numeros)
  print(f"Los numeros primos son {numeros_primos}")

  sumatoria,promedio = obtener_sumatoria_promedio(lista_numeros)
  print(f"La sumatoria da un total de: {sumatoria} y el promedio es: {promedio}")
  mostrar_factorial(lista_numeros)

main()