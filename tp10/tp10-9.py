cadena_caracteres = "10011011"
largo_cadena = len(cadena_caracteres)

res = 0
for indice in range(largo_cadena):
  caracter_actual = cadena_caracteres[indice]
  if(caracter_actual == "1"):
    calculo = 2 ** (largo_cadena - 1 - indice)
    res = res + calculo
  
