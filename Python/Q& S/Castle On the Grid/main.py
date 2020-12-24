
#X se desplaza de abajo a arriba
#Y se desplaza de izq a der

def minimumMoves(grid, startX, startY, goalX, goalY):

    currentX = startX
    currentY = startY
    nextp = ""

    while (currentX != goalX and currentY != goalY):
        #Go to the left
        if nextp == "" or 

def cangodir(grid, currentX, currentY):
    
    posdir = [0,0,0,0]
    #¿Se puede desplazar a la izquierda?
    if ((currentY - 1) < 0 or grid[currentX][currentY - 1] == "X"):
        posdir[0] = 0
    else :
        posdir[0] = 1

    #¿Se puede desplazar a la derecha?
    if ((currentY + 1) == len(grid) or grid[currentX][currentY + 1] == "X"):
        posdir[1] = 0
    else :
        posdir[1] = 1
    
    #¿Se puede desplazar arriba?
    if ((currentX - 1) < 0 or grid[currentX - 1][currentY] == "X"):
        posdir[2] = 0
    else :
        posdir[2] = 1
        
    #¿Se puede desplazar abajo?
    if ((currentX + 1) == len(grid) or grid[currentX + 1][currentY] == "X"):
        posdir[3] = 0
    else :
        posdir[3] = 1







        
