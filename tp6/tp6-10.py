teeth_brushed = 0
hygienic = False
no_brushed_days = 0
more_than_three_brushed_days = 0
brushed_avg = 0  
for day_number in range(1,8):
  times_brushed = int(input(f"Cuantas veces se lavó los dientes el día {day_number}\n> "))
  if(times_brushed > 1): hygienic = True
  if(times_brushed < 1): no_brushed_days+=1
  if(times_brushed >= 3): more_than_three_brushed_days+=1
  brushed_avg += times_brushed

if(not hygienic): print("Higiene insuficiente")
if(more_than_three_brushed_days > 0): print(f"Se cepilló 3 o más veces {more_than_three_brushed_days} días")
brushed_avg //= 7
print(f"Promedio de cepilladas diarias: {brushed_avg}")
if(no_brushed_days > 0): print(f"No se cepilló {no_brushed_days} días")