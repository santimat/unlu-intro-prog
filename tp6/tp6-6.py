max = 0
for i in range(1,12):
  number = int(input("Ingrese un numero: "))
  if (number > max): max,position = number,i

print(f"el numero maximo es: {max} en la posición: {position}")