text = input("Escribe algo: ")

if text.isdigit():
  print("Son todos numeros")
elif text.isalpha():
  print("Son solo letras")
else:
  print("Son letras y numeros")