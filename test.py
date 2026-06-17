def linear_search(word, wordToFind):
  position = -1
  for i in range(len(word)):
    if(word[i].lower() == wordToFind.lower() and position == -1): 
      position = i
  return position

def main():
  word = ["santino", "juan", "santiago", "bernardo"]
  wordToFind = "benjamin"
  position = linear_search(word,wordToFind)
  if(position != -1): 
    print(f"El resultado está en la posición {position + 1}")  
  else:
    print("No se encontró en la lista")

main()
