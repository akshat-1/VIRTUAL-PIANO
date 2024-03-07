import mediapipe as mp
import cv2
import numpy as np
import uuid
import os


offset =int(273/2)
# 1 cm = 45.454545 px as in opencv
class pianokeys():
    # def __init__(self, text , pos,bottom):
    #     self.text = text
    #     self.pos = pos
    #     self.bottom = bottom
        
    def draw(self , image, i):
         cv2.rectangle(image,(103 -12 + 95*i,409- offset) , (148-12+ 95*i +4,682 -offset) , (255,255,255), cv2.FILLED) # middle part
         cv2.rectangle(image,(80 -12+ 95*i +4,591 - offset) , (103-12+ 95*i +4,682-offset) , (255,255,255), cv2.FILLED) # begining part
         cv2.rectangle(image,(148-12+ 95*i +4,591 - offset) , (171-12+ 95*i +4,682 -offset) , (255,255,255), cv2.FILLED) #ending part


    

mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands

cap = cv2.VideoCapture(0)
cap.set(3,1900)
cap.set(4,1080)

with mp_hands.Hands(min_detection_confidence=0.8, min_tracking_confidence=0.5) as hands: 
    while cap.isOpened():
        ret, frame = cap.read()
        

        # BGR 2 RGB
        image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        
        # Flip on horizontal
        image = cv2.flip(image, 1)
       
        
        # Set flag
        image.flags.writeable = False
        
        # Detections
        results = hands.process(image)
        
        # Set flag to true
        image.flags.writeable = True
        
        # RGB 2 BGR
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        
        # Detections
        print(results)
    #start
        cv2.rectangle(image,(0,409 -offset) , (45,682 - offset) , (0,0,0), cv2.FILLED) 
        cv2.rectangle(image,(45,409+182 - offset) , (45+23,682 - offset) , (0,0,0), cv2.FILLED)
    #loop
        for i in range(12):
            keys = pianokeys()

            keys.draw(image , i )
        
    #end
        cv2.rectangle(image,(1204+23+8,409 - offset) , (1204+23+45+8,682- offset) , (0,0,0), cv2.FILLED)
        cv2.rectangle(image,(1204+8,409+182- offset) , (1204+23+8,682 -offset) , (0,0,0), cv2.FILLED)


        
        # Rendering results
        if results.multi_hand_landmarks:
            for num, hand in enumerate(results.multi_hand_landmarks):
                mp_drawing.draw_landmarks(image, hand, mp_hands.HAND_CONNECTIONS, 
                                        mp_drawing.DrawingSpec(color=(121, 22, 76), thickness=2, circle_radius=4),
                                        mp_drawing.DrawingSpec(color=(250, 44, 250), thickness=2, circle_radius=2),
                                         )
            
        
        cv2.imshow('Hand Tracking', image)

        if cv2.waitKey(10) & 0xFF == ord('q'):
            break
cap.release()
cv2.destroyAllWindows()

os.mkdir('Output Images')

cap = cv2.VideoCapture(0)





# with mp_hands.Hands(min_detection_confidence=0.8, min_tracking_confidence=0.5) as hands: 
#     while cap.isOpened():
#         ret, frame = cap.read()
        
#         # BGR 2 RGB
#         image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        
#         # Flip on horizontal
#         image = cv2.flip(image, 1)
        
#         # Set flag
#         image.flags.writeable = False
        
#         # Detections
#         results = hands.process(image)
        
#         # Set flag to true
#         image.flags.writeable = True
        
#         # RGB 2 BGR
#         image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        
#         # Detections
#         print(results)
        
#         # Rendering results
#         if results.multi_hand_landmarks:
#             for num, hand in enumerate(results.multi_hand_landmarks):
#                 mp_drawing.draw_landmarks(image, hand, mp_hands.HAND_CONNECTIONS, 
#                                         mp_drawing.DrawingSpec(color=(121, 22, 76), thickness=2, circle_radius=4),
#                                         mp_drawing.DrawingSpec(color=(250, 44, 250), thickness=2, circle_radius=2),
#                                          )
            
#         # Save our image 
#         if cv2.waitKey(10) & 0xFF == ord('q'):
#             break

# cap.release()
# cv2.destroyAllWindows()