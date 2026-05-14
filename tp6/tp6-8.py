maxRainfall = 0
day = 0
average = 0
for i in range(1,8):
  rainfall = float(input(f"Ingrese los ml para el día {i}: "))
  if(rainfall > maxRainfall): maxRainfall, day = rainfall,i
  average += rainfall 

if(day == 1): print(f"El día con más precipitaciones fue el domingo con: {maxRainfall}ml") 
elif(day == 2): print(f"El día con más precipitaciones fue el lunes con: {maxRainfall}ml") 
elif(day == 3): print(f"El día con más precipitaciones fue el martes con: {maxRainfall}ml") 
elif(day == 4): print(f"El día con más precipitaciones fue el miercoles con: {maxRainfall}ml") 
elif(day == 5): print(f"El día con más precipitaciones fue el jueves con: {maxRainfall}ml") 
elif(day == 6): print(f"El día con más precipitaciones fue el viernes con: {maxRainfall}ml") 
else: print(f"El día con más precipitaciones fue el sabado con: {maxRainfall}ml") 
average //= 7
print(f"El promedio de ml es {average}")