import math

def repeatedString(s,n):
    longitud = len(s)
    nas = 0
    if (longitud == 1 and s == "a"):
        nas = n


    elif (n > longitud):
        fas = find_as(s)
        piso = math.floor(n/longitud)
        rest = n - longitud*piso
        check = 0
        while (check != rest):
            if (s[check] == 'a'):
                nas = nas + 1            
            check = check + 1
        nas = nas + find_as(s)*piso

    elif (n == longitud):
        nas = find_as(s)

    elif (n < longitud):
        index = 0
        while (index < n):
            if (s[index] == "a"):
                nas = nas + 1
            index = index + 1    
        
    #print ("numero de as: "+ str(nas))
    return nas




def find_as(field): 
    a = 0   
    for letra in field :
        if letra == "a":
            a = a + 1
    return a


repeatedString('daaial', 3)
