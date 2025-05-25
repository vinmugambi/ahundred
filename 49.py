f = open('record.txt', 'r')

while True:
  contents = f.readline().strip()
  if contents == "":
    break
  print(contents)

f.close()
