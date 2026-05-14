number = input("Ingrese un numero entre 1 y 100\n> ")

while(not number.isnumeric() or int(number) < 1 or int(number) > 100 ):
  number = input("Ingrese un numero válido entre 1 y 100\n> ")

print(f"{number} es válido")