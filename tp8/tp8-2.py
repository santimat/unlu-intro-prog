age = input("Ingrese su edad, valido solo para edades entre 18 y 60\n> ")

while(not age.isnumeric() or int(age) < 18 or int(age) > 60):
  age = input("Intente de nuevo, valido solo para edades entre 18 y 60\n> ")

print(f"Tenés {age} años, bien ahi 👍")