max = 0
min = 0

for i in range(1,12):
  number = int(input("Ingrese un numero: "))
  if(i == 1): min,positionMin = number,i
  elif (number > max): max,positionMax = number,i
  elif(number < min): min,positionMin = number,i

print(f"el numero maximo es: {max} en la posición: {positionMax}")
print(f"el numero maximo es: {min} en la posición: {positionMin}")