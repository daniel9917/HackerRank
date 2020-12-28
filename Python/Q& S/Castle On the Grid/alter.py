def minimumMoves(grid, startX, startY, goalX, goalY):

    currentX = startX
    currentY = startY
    nextp = ""
    avmoves = []
    nmoves = 0

    #while (currentX != goalX and currentY != goalY):
    avmoves = cangodir(grid, currentX, currentY)
    i = 0
    for el in avmoves :
        if el == 1 :
            while (hasNext(grid, currentX, currentY, i):
                arr = move(currentX, currentY, i)
                currentX = arr [0]
                currentY = arr [1]
            nmoves = nmoves + 1
            if ((cangodir(grid, currentX, currentY) - createm(i)) != [0,0,0,0]):
                minimumMoves(grid, currentX, currentY, goalX, goalY)            
        i = i + 1

def createm (dir):
    if dir == 0:
        return ([1,0,0,0])
    elif dir == 1:
        return ([0,1,0,0])
    elif dir == 2:
        return ([0,0,1,0])
    elif dir == 3:
        return ([0,0,0,1])
    else :
        return ([0,0,0,0])


def cangodir(grid, currentX, currentY):
    
    posdir = [0,0,0,0]

    
    #¿Se puede desplazar arriba?
    if ((currentX - 1) < 0 or grid[currentX - 1][currentY] == "X"):
        posdir[0] = 0
    else :
        posdir[0] = 1
        
    #¿Se puede desplazar abajo?
    if ((currentX + 1) == len(grid) or grid[currentX + 1][currentY] == "X"):
        posdir[1] = 0
    else :
        posdir[1] = 1

    #¿Se puede desplazar a la izquierda?
    if ((currentY - 1) < 0 or grid[currentX][currentY - 1] == "X"):
        posdir[2] = 0
    else :
        posdir[2] = 1

    #¿Se puede desplazar a la derecha?
    if ((currentY + 1) == len(grid) or grid[currentX][currentY + 1] == "X"):
        posdir[3] = 0
    else :
        posdir[3] = 1

    return posdir

def move(currentX, currentY, dir):
    newpos= [currentX,currentY]
    #move one pos up
    if dir == 0:
        newpos [0] = currentX - 1
        newpos [1] = currentY
        return new pos
    #move one pos down
    elif dir == 1:
        newpos [0] = currentX + 1
        newpos [1] = currentY
        return new pos        
    #move one pos left
    elif dir == 2:    
        newpos [0] = currentX
        newpos [1] = currentY - 1
        return new pos           
    #move one pos right
    elif dir == 3:
        newpos [0] = currentX
        newpos [1] = currentY + 1
        return new pos   
    #no move
    else :
        return newpos



def hasNext(grid, currentX, currentY, way):
    #Way up
    if (way == 0):
        if (currentX - 1 >= 0 and grid[currentX + 1][currentY] != "X"):
            return 1
        else :
            return 0
    #Way down
    elif (way == 1):
        if (currentX + 1 < len(grid) and grid[currentX + 1][currentY] != "X"):
            return 1
        else :
            return 0
    #Way left
    elif (way == 2):
        if (currentY - 1 >= 0 and grid[currentX][currentY - 1] != "X"):
            return 1
        else :
            return 0            
    #Way right
    elif (way == 3):
        if (currentY + 1 < len(grid) and grid[currentX][currentY + 1] != "X"):
            return 1
        else:
            return 0
    else :
        return 0