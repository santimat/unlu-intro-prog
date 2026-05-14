temperature = input("Ingrese una temperatura en celsius entre -18 y 50\n> ")

while(not temperature.isnumeric() or int(temperature) < -18 or int(temperature) > 50 ):
  temperature = input("Ingrese una temperatura valida entre -18 y 50\n> ")

print(f"Hacen {temperature}°C")
