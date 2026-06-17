def obtener_mayor_menor_igual(lista_numeros,k): 
  mayor,menor,igual = [],[],[]

  for numero in lista_numeros: 
    if(numero < k):
      menor.append(numero)
    elif(numero > k):
      mayor.append(numero)
    else:
      igual.append(numero)

  return mayor,menor,igual

def obtener_multiplos(lista_numeros,k):
  multiplos = []
  for numero in lista_numeros:
    if(numero % k == 0): 
      multiplos.append(numero)

  return multiplos


def main():
  lista_numeros= [5,7,14,13,3,1,15,17]
  k = 5
  mayor,menor,igual = obtener_mayor_menor_igual(lista_numeros,k)
  print(f"Los numeros mayores a {k} son: {mayor}")
  print(f"Los numeros menores a {k} son: {menor}")
  print(f"Los numeros iguales a {k} son: {igual}")
  multiplos_de_k = obtener_multiplos(lista_numeros,k)
  print(f"Los multiplos de {k} son {multiplos_de_k}")

main()