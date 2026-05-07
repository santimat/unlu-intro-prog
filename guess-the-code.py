# Descripción:
# Imagina que estás intentando descifrar la clave de un candado digital antiguo. 
# Este candado tiene 3 ranuras y cada ranura puede contener un dígito del 0 al 9.

# Se sabe que la combinación ganadora cumple con las siguientes condiciones:

# La suma de los tres dígitos debe ser exactamente igual a 15.
# El primer dígito debe ser un número par.
# El tercer dígito debe ser mayor que el segundo.

# Tu misión:
# Escribe un programa en Python que encuentre y muestre por pantalla todas las combinaciones posibles que cumplan con estas tres reglas.

counter = 1
for a in range(0,10, 2):
  for b in range(0,10):
    for c in range(0,10):
        if c > b:
           sum = a + b + c
           if sum == 15:
            print(f"{counter}")
            counter += 1
            print(a,b,c)