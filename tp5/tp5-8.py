side_a = float(input("Ingrese el primer lado: "))
side_b = float(input("Ingrese el segundo lado: "))
base = float(input("Ingrese la base del triangulo: "))

if side_a == side_b and side_a == base:
  print("Triangulo equilatero")
elif side_a == side_b: 
  print("Triangulo isósceles")
else: 
  print("Triangulo escaleno")
