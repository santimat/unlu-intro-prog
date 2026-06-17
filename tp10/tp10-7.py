def obtener_numero():
  # numero = int(input("Ingrese un numero largo"))
  numero = 1234567890
  return numero

def formatear_numero(numero):
  numero_string = str(numero)
  numero_formateado = ""
  largo = len(numero_string)

  for indice in range(largo - 1, -1, -1):
    distancia = (largo - 1) - indice

    if(distancia % 3 == 0 and indice != largo -1):
      numero_formateado = numero_string[indice] +"." + numero_formateado
    else:
      numero_formateado = numero_string[indice] + numero_formateado

  return numero_formateado


def main():
  numero = obtener_numero()
  numero_formateado = formatear_numero(numero)
  print(f"El numero formateado quedaría:")
  print(numero_formateado)

main()