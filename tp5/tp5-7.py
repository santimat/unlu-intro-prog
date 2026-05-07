note1 = float(input("Ingrese la nota de su primer parcial: "))
note2 = float(input("Ingrese la nota de su segundo parcial: "))

average = (note1 + note2) / 2

if note1 >= 4 and note2 >= 4:
  if average >= 7:
    print("Promocinaste crack")
  else: 
    print("Sos un inservible")
if note1 <= 4 or note2 <= 4:
  print("recursá pa")