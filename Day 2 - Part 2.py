import copy
def loopThrough(start: int, end: int):
  x=0
  listofopcodes = copy.deepcopy(opcodes)
  
  listofopcodes[1] = start
  listofopcodes[2] = end
  while True:
    try:
      if listofopcodes[x] == 1:
        listofopcodes[listofopcodes[x+3]] = listofopcodes[listofopcodes[x+1]] + listofopcodes[listofopcodes[x+2]]
      elif listofopcodes[x] == 2:
        listofopcodes[listofopcodes[x+3]] = listofopcodes[listofopcodes[x+1]] * listofopcodes[listofopcodes[x+2]]
      if listofopcodes[0] == 19690720:
        print(str(start) + " " + str(end))
    except:
      break
    x+=4

    
with open("input.txt", "r") as f:
  data = f.read()
opcodes = data.split(",")
for i in range(0, len(opcodes)): 
    opcodes[i] = int(opcodes[i])

for i in range(0, 100):
  for j in range (0, 100):
    loopThrough(i, j)