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
# este for es de paso 2, para cumplir la condición de que el primer numero debe ser par
for a in range(0,10, 2):
  for b in range(0,10):
    for c in range(0,10):
        sum = a + b + c
        # el tercer numero mayor que el segundo
        # si la suma nos da 15
        if c > b and sum == 15:
           # suma de los 3 numeros
            # numero de combinación
            print(f"{counter}")
            # aumento en uno el contador de combinaciones
            counter += 1
            # muestro los 3 digitos que funcionan
            print(a,b,c)
