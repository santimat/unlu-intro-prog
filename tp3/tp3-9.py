# valor de cada moneda en pesos
dollar = 1450
real = 260.3
euro = 1575.5

balance = 10000

print(f"Usted cuenta con ${balance} pesos argentinos eso equivalen a:")
# round sirve para redondear un tipo de dato flotando, y el 2 es para decirle que queremos 2 decimales
print(f"{round(balance / dollar,2)} dolares")
print(f"{round(balance / real,2)} reales")
print(f"{round(balance / euro,2)} euros")