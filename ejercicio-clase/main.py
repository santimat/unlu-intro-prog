# Se desea registrar y analizar el desempeño del equipo de Handball de la UNLu en el Campeonato 2026. Para ello, se solicita escribir, en Python, las funciones necesarias con sus correspondientes parámetros por valor o referencia -según corresponda-, para realizar las siguientes tareas:
# a)    Definir y cargar en la estructura de datos adecuada el resultado de los 20 partidos del torneo de la siguiente manera: ‘T’ triunfo, ‘D’ derrota, ‘E’ empate y ‘N’ no jugado. Se debe validar que el carácter ingresado sea válido.
# b)    Desarrollar una función que retorne un booleano al programa principal indicando true en caso de que el equipo haya jugado todos los partidos del campeonato y false en caso contrario.
# c)    Escribir una función que calcule y retorne la cantidad de puntos obtenidos durante el campeonato teniendo en cuenta que por cada victoria se obtienen 3 puntos y por cada empate 1 punto.
# d)    Escribir una función que informe el porcentaje de partidos ganados, perdidos, empatados y no jugados durante el campeonato.


def main(): 
  games = fill_games(5)
  
  play_every_game = every_game(games)
  if(play_every_game):
    print("Se jugaron todos los partidos")
  else:
    print("No se jugaron todos los partidos")

  points = getPoints(games)
  print(f"Se hicieron {points} puntos")

  show_percentages(games)
  


def fill_games(number_games):
  games = []

  print("Triunfo: T, Empate: E, Derrota: D, No jugó: N")
  
  for i in range(number_games):
    result = input(f"Ingrese la letra correspondiente para el partido {i + 1}\n> ")

    while(result.upper() != "T" and result.upper() != "E" and result.upper() != "D" and result.upper() != "N"):
      result = input("Letra no valida intenten de nuevo\n> ")

    games.append(result.upper())

  return games
    
def every_game(games):
  flag = True
  idx = 0
  while(idx < len(games) and flag):
    if(games[idx] == "N"): 
      flag = False
    idx += 1
  
  return flag

def getPoints(games):
  points = 0
  for game in games:
    if(game == "T"):
      points += 3
    elif(game == "E"):
      points +=1

  return points

def show_percentages(games):
  t = 0
  d = 0
  e = 0
  n = 0
  for game in games:
    if(game == "T"):
      t += 1
    elif(game == "D"):
      d += 1
    elif(game == "E"):
      e += 1
    else:
      n +=1

  t = (t / len(games)) * 100
  d = (d / len(games)) * 100
  e = (e / len(games)) * 100
  n = (n / len(games)) * 100
  print(f"El porcentaje de triunfos es: {t}")
  print(f"El porcentaje de derrotas es: {d}")
  print(f"El porcentaje de empates es: {e}")
  print(f"El porcentaje de partidos no jugados es: {n}")

main()
