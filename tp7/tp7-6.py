secret_number = 4
lower_times = 0
upper_times = 0
tries = 1
number = input("Adivine el numero entre 1 y 10\n> ")

while(int(number) != secret_number or not number.isnumeric()):
  if(int(number) < secret_number): lower_times+=1
  else: upper_times+=1
  tries+=1
  number = input("Intente otro numero\n> ")

print(f"Adivinaste!!! 🎉🎉 el numero era {secret_number}")  
print(f"Numero de intentos: {tries}")
if(lower_times >0): print(f"{lower_times} veces se estuvo por debajo del numero")
if(upper_times >0): print(f"{upper_times} veces se estuvo por encima del numero")
