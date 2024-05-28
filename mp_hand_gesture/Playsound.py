import cv2 
from shapely.geometry import Point
from shapely.geometry.polygon import Polygon
from playsound import playsound
import numpy as np
from playsound2 import get_node
#define a classwhise function is to indentify where the finger is pointing and play sound only once

offset = int(273)
class node(): 
    # is_discont = False
    is_playing =False
    # contu = [ [(0,409 -offset) , (45 , 409 - offset) , (45 , 591 - offset) , (68,591 - offset) , (68,727 - offset), (0,727 - offset)],
    #           [(45,409 - offset) ,(91,409-offset), (91,591 - offset) , (45 , 591 -offset)]
    #         ]
     #making a constructor
    def __init__(self , vis   , pointI, pointM, pointR, pointT, contu):
        self.vis = vis  
        # self.is_playing = is_playing  
        self.index = pointI
        self.middle = pointM
        self.ring = pointR
        self.thumb = pointT
        self.contu = contu

        # for i in range(12):
        #     if(i != 1 and i!= 5 and i!= 8 and self.is_discont == False):
        #         self.contu.append([(91 + 95*i,409- offset) ,(140+ 95*i , 409 -offset),(140+ 95*i,591 - offset),(163+95*i , 591 - offset), (163+ 95*i,727 -offset) , (72 + 95*i, 727 -offset),(72+ 95*i,591 - offset),(91 + 95*i , 591 - offset)])
        #         self.contu.append([(45 + (i+1)*95 ,409 - offset) ,(91 + (i+1)* 95,409 - offset), (91 + (i+1)* 95 , 591 - offset) , (45 + (i+1)*95 ,591 - offset)])
        #     elif(i != 1 and i!= 5 and i!= 8 and self.is_discont == True):
        #         self.contu.append([(72+ 95*i,409- offset) ,(140+ 95*i , 409 -offset),(140+ 95*i,591 - offset),(163+95*i , 591 - offset), (163+ 95*i,727 -offset) , (72 + 95*i, 727 -offset)])
        #         self.contu.append([(45 + (i+1)*95 ,409 - offset) ,(91 + (i+1)* 95,409 - offset), (91 + (i+1)* 95 , 591 - offset) , (45 + (i+1)*95 ,591 - offset)])
        #         self.is_discont = False
        #     else:
        #         self.contu.append([(91 + 95*i,409- offset) ,(163+95*i , 409 -offset), (163+ 95*i,727 -offset) , (72 + 95*i, 727 -offset),(72+ 95*i,591 - offset),(91 + 95*i , 591 - offset)])
        #         self.is_discont = True

        # self.contu.append([(1235,409 - offset), (1280 , 409-offset) , (1280,727- offset),(1212,727-offset) , (1212, 591 -offset) , (1212 +23 , 591-offset)])

                


    
    #methord
    def play(self):
         j=0
         pointI  = Point(self.index[0] , self.index[1])
         pointM  = Point(self.middle[0] , self.middle[1])
         pointR  = Point(self.ring[0] , self.ring[1])
         pointT  = Point(self.thumb[0] , self.thumb[1])
       
         for i in self.contu:
            polygon = Polygon(i)
            if( (polygon.contains(pointI) == 1 or polygon.contains(pointM) == 1 or polygon.contains(pointR) == 1 or polygon.contains(pointT) == 1) and self.vis[j] == False):
                 self.vis[j] = True
                 get_node(j)
            if((not polygon.contains(pointI)) == 1 and (not polygon.contains(pointM)) == 1 and (not polygon.contains(pointR)) == 1 and (not polygon.contains(pointT)) == 1):
               if(self.vis[j]):
                self.vis[j] = False

            j+=1
        
            
        
            
#algo -> for every frame we will run a loop through all the conturs which will check that finger is pointing in which contour. and in main file we will make a call for each finger  



        


    