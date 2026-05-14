days = int(input("Cuantos días caminó con su perro?\n> "))
average = 0
max_blocks_walked,day_max = 0, 0
more_than_thirty_blocks = False
more_than_twenty_blocks = False
accumulator_days = 0

for day in range(1,days + 1):
  blocks = int(input(f"Cuantas cuadras caminó el día {day}?\n> "))
  if(blocks > 30): more_than_thirty_blocks = True
  if(blocks > 20): more_than_twenty_blocks = True
  if(blocks > max_blocks_walked): max_blocks_walked, day_max = blocks, day
  average+= blocks
  accumulator_days += blocks

average //= days
print(f"Promedio de cuadras por día: {average}")
if(more_than_thirty_blocks): print("El perro debe descansar 24hs 💤")
if(average < 10 and not more_than_twenty_blocks): print("El perro debe caminar más 🦮") 
print(f"El día que más se caminó fue el día {day_max} y se caminaron: {max_blocks_walked} cuadras")
print(f"Se caminó 🚶 un total de {accumulator_days} cuadras")