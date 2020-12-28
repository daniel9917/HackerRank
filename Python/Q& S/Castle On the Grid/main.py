
#X se desplaza de abajo a arriba
#Y se desplaza de izq a der

def main():  

    n = int(input())

    grid = []

    for _ in range(n):
        grid_item = input()
        grid.append(grid_item)

    startXStartY = input().split()

    startX = int(startXStartY[0])

    startY = int(startXStartY[1])

    goalX = int(startXStartY[2])

    goalY = int(startXStartY[3])

    result = minimumMoves(grid, startX, startY, goalX, goalY)

    print (result)



def goThisWay (grid, ways, currentX, currentY):    
    index = 0
    dir = 0
    while (index < len(ways))        
        if ways[index] == 1 :
            while (hasNext(grid, currentX, currentY, index)):

        index = index + 1


def minimumMoves(grid, startX, startY, goalX, goalY):

    currentX = startX
    currentY = startY
    nextp = ""
    avmoves = []

    #while (currentX != goalX and currentY != goalY):
    avmoves = cangodir(grid, currentX, currentY)
    
    

    return avmoves
        
def find (grid, startX, startY, goalX, goalY):
    nmoves = 0
    i = 0
    amoves = cangodir(grid, currentX, currentY)
    while (i < len(amoves)):
        for el in amoves:
            if el == 1 :
                while (hasNext(grid, currentX, currentY, i)):
                    

        i = i + 1

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




main()




        
