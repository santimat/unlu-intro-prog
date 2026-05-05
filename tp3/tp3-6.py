num1= 2
num2 = 3

print(f"La variable num1 vale: {num1} y num2 vale: {num2}")

# Guardamos el valor de la variable num1 en una variable auxiliar para no perderla a la hora de reescribir
temp = num1
num1 = num2
num2 = temp

print(f"Luego del cambio la variable num1 vale: {num1} y num2 vale: {num2}")

