import time
import random

xsize = 156
ysize = 44

dish = [[" " for x in range(ysize)] for y in range(xsize)] 
tempDish  = [[" " for x in range(ysize)] for y in range(xsize)] 

randomGen = True
customGen = False
crosshair = False
glider = False
hex3 = False
blinker = False

delay =0.1

def printDish():
    line = ""
    for i in range(0,ysize):
        for i2 in range(0,xsize):
            line+=dish[i2][ysize-1-i]
        line+='\n'
    print(line)
    
def checkNeighbours(index1, index2):
    
    x1 = index1-1
    x2 = index1
    x3 = index1+1
    
    y1 = index2-1
    y2 = index2
    y3 = index2+1

    aliveNeighbours = 0
    
    if x1 == -1:
        x1 = xsize-1
    if x3 == xsize:
        x3 = 0
    if y1 == -1:
        y1 = ysize-1
    if y3 == ysize:
        y3 = 0

    if dish[x1][y1] == "#":
        aliveNeighbours +=1
    if dish[x1][y2] == "#":
        aliveNeighbours +=1
    if dish[x1][y3] == "#":
        aliveNeighbours +=1
    if dish[x2][y1] == "#":
        aliveNeighbours +=1
    if dish[x2][y3] == "#":
        aliveNeighbours +=1
    if dish[x3][y1] == "#":
        aliveNeighbours +=1
    if dish[x3][y2] == "#":
        aliveNeighbours +=1
    if dish[x3][y3] == "#":
        aliveNeighbours +=1
    
    if dish[x2][y2] == "#" and (aliveNeighbours < 2 or aliveNeighbours > 3):
        tempDish[x2][y2] = " "
    if dish[x2][y2] == " " and aliveNeighbours == 3:
        tempDish[x2][y2] = "#"

for i in range(0,ysize):
    for i2 in range(0,xsize):
        randNumber = random.randint(0, 2)
        if randNumber == 1:
            dish[i2][i] = "#"
        else:
            dish[i2][i] = " "
        if randomGen == False:
            dish[i2][i] = " "
            
if crosshair == True:
    dish[75][20] = "#"
    dish[76][20] = "#"
    dish[74][20] = "#"
    dish[75][21] = "#"
    
if glider == True:
    dish[75][20] = "#"
    dish[76][20] = "#"
    dish[74][20] = "#"
    dish[76][21] = "#"
    dish[75][22] = "#"
    
if hex3 == True:
    dish[78][20] = "#"
    dish[77][21] = "#"
    dish[77][19] = "#"
    dish[76][18] = "#"
    dish[76][22] = "#"
    dish[75][22] = "#"
    dish[75][18] = "#"
    dish[74][22] = "#"
    dish[74][18] = "#"
    dish[73][21] = "#"
    dish[73][19] = "#"
    dish[72][20] = "#"
if blinker == True:
    dish[78][20] = "#"
    dish[77][20] = "#"
    dish[77][21] = "#"
    dish[78][21] = "#"
    dish[79][22] = "#"
    dish[79][23] = "#"
    dish[80][22] = "#"
    dish[80][23] = "#"
if customGen == True:
    try:
        dreams = True
        while dreams:
            xIn = int(input("X?"))
            yIn = int(input("Y?"))
            if dish[xIn][yIn] == "#":
                dish[xIn][yIn] = " "
            elif dish[xIn][yIn] == " ":
                dish[xIn][yIn] = "#"
    except ValueError:
        dreams = False
        
printDish()
time.sleep(3)

memes = True
while memes:
    tempDish = [x[:] for x in dish]
    for i in range(0,ysize):
        for i2 in range(0,xsize):
            checkNeighbours(i2, i)
    dish = [x[:] for x in tempDish]
    printDish()
    time.sleep(delay)
