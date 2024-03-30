import cv2 
from shapely.geometry import Point
from shapely.geometry.polygon import Polygon
from playsound import playsound
import numpy as np
from playsound2 import get_node
#define a classwhise function is to indentify where the finger is pointing and play sound only once

offset = int(273)
class node(): 
    is_discont = False
    is_playing =False
    contu = [ [(0,409 -offset) , (45 , 409 - offset) , (45 , 591 - offset) , (68,591 - offset) , (68,727 - offset), (0,727 - offset)],
              [(45,409 - offset) ,(91,409-offset), (91,591 - offset) , (45 , 591 -offset)]
            ]
     #making a constructor
    def __init__(self , is_playing   , point):
        self.is_playing = is_playing
         
        self.point = point
        for i in range(12):
            if(i != 1 and i!= 5 and i!= 8 and self.is_discont == False):
                self.contu.append([(91 + 95*i,409- offset) ,(140+ 95*i , 409 -offset),(140+ 95*i,591 - offset),(163+95*i , 591 - offset), (163+ 95*i,727 -offset) , (72 + 95*i, 727 -offset),(72+ 95*i,591 - offset),(91 + 95*i , 591 - offset)])
                self.contu.append([(45 + (i+1)*95 ,409 - offset) ,(91 + (i+1)* 95,409 - offset), (91 + (i+1)* 95 , 591 - offset) , (45 + (i+1)*95 ,591 - offset)])
            elif(i != 1 and i!= 5 and i!= 8 and self.is_discont == True):
                self.contu.append([(72+ 95*i,409- offset) ,(140+ 95*i , 409 -offset),(140+ 95*i,591 - offset),(163+95*i , 591 - offset), (163+ 95*i,727 -offset) , (72 + 95*i, 727 -offset)])
                self.contu.append([(45 + (i+1)*95 ,409 - offset) ,(91 + (i+1)* 95,409 - offset), (91 + (i+1)* 95 , 591 - offset) , (45 + (i+1)*95 ,591 - offset)])
                self.is_discont = False
            else:
                self.contu.append([(91 + 95*i,409- offset) ,(163+95*i , 409 -offset), (163+ 95*i,727 -offset) , (72 + 95*i, 727 -offset),(72+ 95*i,591 - offset),(91 + 95*i , 591 - offset)])
                self.is_discont = True

        self.contu.append([(1235,409 - offset), (1280 , 409-offset) , (1280,727- offset),(1212,727-offset) , (1212, 591 -offset) , (1212 +23 , 591-offset)])

                


    
    #methord
    def play(self):
        j =0
        points  = Point(self.point[0] , self.point[1])
       
        for i in self.contu:
            polygon = Polygon(i)
            if( polygon.contains(points) == 1 and self.is_playing == False):
                self.is_playing = True
                get_node(j)
            elif(polygon.contains(points) == -1 ):
                self.is_playing = False
            j += 1
            
        
            
#algo -> for every frame we will run a loop through all the conturs which will check that finger is pointing in which contour. and in main file we will make a call for each finger  



        


    