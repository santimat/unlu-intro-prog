decimal = float(input("Ingresa un numero con decimales: "))
nearestInt = round(decimal)
twoDecimals = round(decimal,2)

print(f"El numero redondeado al entero más cercano: {nearestInt}")
print(f"El numero redondeado con 2 decimales: {twoDecimals}")