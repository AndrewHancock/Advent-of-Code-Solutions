import matplotlib.pyplot as plt

with open("input.txt", "r") as f:
  data = f.readlines()

currentX = currentY = newX = newY = 0

line1Instructions = data[0].split(",")
line2Instructions = data[1].split(",")
line1XCoords = [0]
line1YCoords = [0]
line2XCoords = [0]
line2YCoords = [0]

for x in line1Instructions:
  if x[:1] == 'U':
    newY = currentY + int(x[1:])
    line1XCoords.append(newX)
    line1YCoords.append(newY)
  elif x[:1] == 'D':
    newY = currentY - int(x[1:])
    line1XCoords.append(newX)
    line1YCoords.append(newY)
  elif x[:1] == 'R':
    newX = currentX + int(x[1:])
    line1XCoords.append(newX)
    line1YCoords.append(newY)
  elif x[:1] == 'L':
    newX = currentX - int(x[1:])
    line1XCoords.append(newX)
    line1YCoords.append(newY)
  currentX, currentY = newX, newY

currentX = currentY = newX = newY = 0
for x in line2Instructions:
  if x[:1] == 'U':
    newY = currentY + int(x[1:])
    line2XCoords.append(newX)
    line2YCoords.append(newY)
  elif x[:1] == 'D':
    newY = currentY - int(x[1:])
    line2XCoords.append(newX)
    line2YCoords.append(newY)
  elif x[:1] == 'R':
    newX = currentX + int(x[1:])
    line2XCoords.append(newX)
    line2YCoords.append(newY)
  elif x[:1] == 'L':
    newX = currentX - int(x[1:])
    line2XCoords.append(newX)
    line2YCoords.append(newY)
  currentX, currentY = newX, newY

intersection = []
# This is where the fun begins
for x in range(len(line1XCoords) - 1):
  # Left to right or right to left
  if line1XCoords[x] < line1XCoords[x + 1] or line1XCoords[x] > line1XCoords[x + 1]:
    if line1XCoords[x] < line1XCoords[x + 1]:
      x1 = line1XCoords[x]
      x2 = line1XCoords[x + 1]
    else:
      x2 = line1XCoords[x]
      x1 = line1XCoords[x + 1]
    # Grab the range and compare to see if crosses
    for y in range(x1, x2):
      # Need to find the proper y, only way for it to cross is if it goes up or down
      # ex. y1 < y2 or y1 > y2
      for j in range(len(line2YCoords) - 1):
        if line2YCoords[j] < line2YCoords[j+1] or line2YCoords[j] > line2YCoords[j+1]:
          # Need to order them correctly for the range
          if line2YCoords[j] < line2YCoords[j+1]:
            y1 = line2YCoords[j]
            y2 = line2YCoords[j+1]
          else:
            y2 = line2YCoords[j]
            y1 = line2YCoords[j + 1]
          # walk through the line and see if it matches at one point the y on the x line
          for k in range(y1, y2):
            if k == line1YCoords[x]:
              intersection.append(line1YCoords[x] + line2XCoords[j])

print(intersection)
