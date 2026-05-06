a = float(input("Ingrese el valor para a: "))
b = float(input("Ingrese el valor para b: "))
c = float(input("Ingrese el valor para c: "))

squareRoot = pow(pow(b,2) - 4*a*c,1/2);
res = (-b + squareRoot) / (2*a)
res2 = (-b - squareRoot) / (2*a)
print(res)
print(res2)