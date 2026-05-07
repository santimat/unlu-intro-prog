decimal = int(input("Ingrese un numero entre 0 y 255: "))

binary = ""
# para los numeros par se agrega un 0 y para los impar un 1
while(decimal != 0):
  if decimal % 2 == 0:
    binary+= "0"
  else: 
    binary+= "1"
  decimal = int(decimal / 2)

inverted = ""
# len() devuelve la cantidad de letras del binario, a este le restamos uno ya que las posiciones de los array arrancan en 0, por lo que terminan uno antes
# terminamos el for en -1 porque la condición es mientas que i > -1 así llegamos al 0
# paso -1 para ir hacia atras 
for i in range(len(binary) - 1, -1, -1):
  # en python los strings son inmutables, por eso almacenamos el texto invertido en una nueva variable
  inverted += binary[i]
print(inverted)