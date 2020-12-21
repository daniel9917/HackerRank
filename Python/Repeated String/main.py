#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the repeatedString function below.
def repeatedString(s, n):
    longitud = len(s)
    if (longitud == 1 and n > longitud)
        return longitud
    elif (longitud == n) :
        #print("same")
        a = find_as(s)
        return a

    elif (longitud > n):
        #print("cut")
        a = find_as(cutstr(s,n))
        return a
        
    elif (longitud < n):
        #print("enlarge")
        a = find_as(enlargestr(s,n))
        return a

def find_as(field):
    nas = 0
    for letra in field :
        if letra == "a":
            nas = nas + 1
    return nas


#fcn used to when n is lower that the lenght of the string
def cutstr (s, n):
    newstr = ""
    index = 0
    for element in s :
        if (index == n) :
            break
        newstr = newstr+element
        index = index + 1
    #print (newstr)
    return newstr
#fcn uses to enlarge the string to the lenght inputed
def enlargestr (s, n):
    newstr = ""
    #print (str(len(s)))
    if len(s) == 1:
        #print ("case 1")
        while (len(newstr) != n) :
            newstr = newstr + s
            #print("enlarging "+str(len(newstr)))

        
    else :
        #print ("case 2")
        while (len(newstr) != n) :
            for letra in s:
                newstr = newstr+letra
                #print("enlarging"+str(len(newstr)))
                if len(newstr) == n :
                    break
        #print (newstr)
    return newstr


#enlargestr('daniel',6)
#cutstr('daniel', 3)
repeatedString('a', 1000000000000)