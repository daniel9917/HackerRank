#!/bin/python3
import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    longitud = len(c)
    print(str(longitud))
    jumps = 0
    end = 0
    index = 0
    while (end != 1):
        print (str(index))
        if (index < (longitud - 2)) :
            if ((c[index + 1] == 0) and (c[index + 2] == 0)) :
                jumps = jumps + 1
                index = index + 2
            elif ((c[index + 1] == 1) and (c[index + 2] == 0)) :
                jumps = jumps + 1
                index = index + 2
            elif ((c[index + 1] == 0) and (c[index + 2] == 1)) :
                jumps = jumps + 1
                index = index + 1
            #print ("index :"+str(index)+" jumps: "+str(jumps)+" end: "+str(end))
        else :
            if (index == (longitud - 1)) :
                if (c[index] == 0) :
                    end = 1
            elif (index == (longitud - 2)) :
                if ((c[index] == 0) and (c[index + 1] == 0)) :
                    jumps = jumps + 1
                    end = 1       
            #print ("index :"+str(index)+" jumps: "+str(jumps)+" end: "+str(end))        
        print (str(index))
    return jumps






if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    c = list(map(int, input().rstrip().split()))

    print ("El numero de saltos necesarios es: "+str(jumpingOnClouds(c)))

    # fptr.write(str(result) + '\n')

    # fptr.close()