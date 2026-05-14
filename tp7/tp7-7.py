import os
option = 1
while (option != 0):
  print("1️⃣: Saludar")
  print("2️⃣: Informar temperatura")
  print("3️⃣: Ver nombre de la materia")
  print("4️⃣: Salir")
  option = input("Seleccione una opción entre [1-4]\n> ")

  if(not option.isnumeric()): print("Valor no valido reintente")
  elif(int(option) == 1): print("Hola como estas crack!👋")
  elif(int(option) == 2): print("La temperatura de hoy es de 30°C un calorazo")
  elif(int(option) == 3): print("Introducción a la programación 🧑‍💻")
  
  if(option != 4): 
    input("Presione el enter para continuar")
    os.system("clear" if os.name == "nt" else "cls")
  else: print("Adios crack!👋")

