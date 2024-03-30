import cv2
import numpy as np

offset =int(273)
class pianokeys():
    # def __init__(self, text , pos,bottom):
    #     self.text = text
    #     self.pos = pos
    #     self.bottom = bottom
        
    def draw(self , image, i):
         cv2.drawContours(image,[np.array([[91 + 95*i,409- offset] ,[140+ 95*i , 409 -offset],[140+ 95*i,591 - offset],[163+95*i , 591 - offset], [163+ 95*i,727 -offset] , [72 + 95*i, 727 -offset],[72+ 95*i,591 - offset],[91 + 95*i , 591 - offset]])] , -1 ,(255,255,255), cv2.FILLED) # middle part
        #  cv2.drawContours(image,[np.array([[72+ 95*i,591 - offset] ,[95+ 95*i,727-offset]])] , -1,(255,255,255), cv2.FILLED) # begining part
        #  cv2.drawContours(image,[np.array([[140+ 95*i,591 - offset] , [163+ 95*i,727 -offset]])] ,-1, (255,255,255), cv2.FILLED) #ending part
    def addblackkeys(self,image,i):
       #take input from draw fxn to add a black key at the position 
        if(i != 1 and i!= 5 and i!= 8):
            cv2.rectangle(image,(45 + (i+1)*95 ,409 - offset) , (91 + (i+1)* 95 , 591 - offset) , (0,0,0), cv2.FILLED)
        else:
            cv2.rectangle(image,(140+ 95*i, 409- offset) , (163+ 95*i, 591 - offset)  , (255,255,255), cv2.FILLED)
            cv2.rectangle(image,(167+ 95*i , 409- offset) , (190+ 95*i , 591 - offset) , (255,255,255), cv2.FILLED)