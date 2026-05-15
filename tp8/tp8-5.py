exit = False
option = ""
while(not exit):
  print("Seleccione su color favorito")
  print("1. Verde")
  print("2. Rojo")
  print("3. Azul")
  color_option = input("> ")
  
  if(not color_option.isnumeric() or int(color_option) < 1 or int(color_option) > 3):
    print("======= COLOR INVALIDO =======")
    print("1. Reintentar")
    print("2. Salir")
    option = input("> ")
  else: exit = True
  if(option.isnumeric() and int(option) == 2): 
    exit = True
    print("Adiós!👋")


if(int(color_option) == 1): print("Te gusta el Verde")
if(int(color_option) == 2): print("Te gusta el Rojo")
if(int(color_option) == 3): print("Te gusta el Azul")