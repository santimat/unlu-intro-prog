name = input("Ingrese un nombre\n> ")
first_name = name
appear_times_first_name = 0
while(name.lower() != "fin" or name.isnumeric()):
  if(name.lower() == first_name.lower()): appear_times_first_name+=1
  name = input("Ingrese otro nombre\n> ")

print(f"El primer nombre '{first_name}' se repite {appear_times_first_name} veces")
