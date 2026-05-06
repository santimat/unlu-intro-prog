lastname = input("Ingrese su apellido: ")
note1 = float(input("Ingrese la nota de su primer parcial: "))
note2 = float(input("Ingrese la nota de su segundo parcial: "))
average = (note1 + note2) / 2

print(f"Alumno: {lastname}")
print(f"Primer parcial: {note1}")
print(f"Segundo parcial: {note2}")
print(f"Promedio: {average}")