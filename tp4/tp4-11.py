num1 = int(input("Ingresa el primer numero: "))
num2 = int(input("Ingresa el segundo numero: "))
num3 = int(input("Ingresa el tercer numero: "))

if num1 > num2 and num1 > num3: 
  print(f"El mayor es el: {num1}")
elif num2 > num3 and num2 > num1: 
  print(f"El mayor es el: {num2}")
else: 
  print(f"El mayor es el: {num3}")

if num1 < num2 and num1 < num3:
  print(f"El menor es: {num1}")
elif num2 < num1 and num2 < num3:
  print(f"El menor es {num2}")
else:
  print(f"El menor es {num3}")

num1_absolute = print(abs(num1))