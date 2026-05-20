def getLength(word):
  length = 0
  for letter in word:
      length+=1
  return length


def main():
  username = input("Ingrese su nombre\n> ")
  trimmed_username = username.replace(" ","")
  print(f"{trimmed_username} tiene {getLength(trimmed_username)} letras")

main()