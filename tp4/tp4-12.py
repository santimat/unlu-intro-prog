seconds = int(input("Ingrese un tiempo en segundos: "))

# 3600 = 1 hour
hours = int(seconds / 3600)
# primero sacamos lo que sobra de la hora
# luego calculamos eso en minutos
minutes = int((seconds % 3600) / 60)
# lo que sobra de pasar segundos a minutos son los segundos
seconds = int(seconds % 60)

print(f"{hours}H {minutes}M {seconds}S")