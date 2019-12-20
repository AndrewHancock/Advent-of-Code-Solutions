def check1st(number) -> bool:
  lastNumber = -1
  for x in range(len(number) - 1):
    if lastNumber == int(number[x:x+1]):
      continue
    elif number[x:x+1] == number[x+1:x+2] and number[x:x+1] !=  number[x+2:x+3]:
        return True
    lastNumber = int(number[x:x+1])
  return False

def check2nd(number) -> bool:
  for x in range(len(number)-1):
    if int(number[x:x+1]) <= int(number[x+1:x+2]):
      if x+2 == len(number):
        return True
    else:
        return False

y = 0
for x in range(145852, 616942):
  if check1st(str(x)) and check2nd(str(x)):
    y += 1
print(y)