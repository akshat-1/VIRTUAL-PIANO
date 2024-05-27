import mediapipe as mp
import cv2
import numpy as np
import os
from pianokeys import pianokeys
from Playsound import node


offset =int(273)
# 1 cm = 45.454545 px as in opencv
is_index = False
is_middle = False
is_ring = False
is_thumb = False



mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands

cap = cv2.VideoCapture(0)
cap.set(3,1900)
cap.set(4,1080)


frameWidth = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
frameHeight = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)

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
        # print(results)
    #start
        # cv2.rectangle(image,(0,409 -offset) , (45,727 - offset) , (255,255,255), cv2.FILLED) 
        # cv2.rectangle(image,(45,591 - offset) , (68,727- offset) , (255,255,255), cv2.FILLED)
        cv2.drawContours(image, [np.array([[0,409 -offset] , [45 , 409 - offset] , [45 , 591 - offset] , [68,591 - offset] , [68,727 - offset], [0,727 - offset]])], -1, (255 , 255 , 255) , cv2.FILLED )
        cv2.drawContours(image,[np.array([[45,409 - offset] ,[91,409-offset], [91,591 - offset] , [45 , 591 -offset]])] , -1 ,(0,0,0), cv2.FILLED)
    #loop
        for i in range(12):
            keys = pianokeys()

            keys.draw(image , i )
            keys.addblackkeys(image , i)
        
    #end
        cv2.drawContours(image,[np.array([[1235,409 - offset], [1280 , 409-offset] , [1280,727- offset],[1212,727-offset] , [1212, 591 -offset] , [1212 +23 , 591-offset]])] ,-1 , (255,255,255), cv2.FILLED)
        # cv2.drawContours(image,[np.array([[1212,591- offset] , [1235,727 -offset]])] ,-1 , (255,255,255), cv2.FILLED)

 
        #need to improve this code using holistic model to detect position on bith the hands simultaniously using left_hand_landmarks and right_hand_landmarks
        # Rendering results
        if results.multi_hand_landmarks:
            for num, hand in enumerate(results.multi_hand_landmarks):
                mp_drawing.draw_landmarks(image, hand, mp_hands.HAND_CONNECTIONS, 
                                        mp_drawing.DrawingSpec(color=(121, 22, 76), thickness=2, circle_radius=4),
                                        mp_drawing.DrawingSpec(color=(250, 44, 250), thickness=2, circle_radius=2),
                                         )
            
            IndexLandmark = results.multi_hand_landmarks[0].landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]
            IndexCoordinatesLandmark = mp_drawing._normalized_to_pixel_coordinates(IndexLandmark.x, IndexLandmark.y, frameWidth, frameHeight)

            MiddleLandmark = results.multi_hand_landmarks[0].landmark[mp_hands.HandLandmark.MIDDLE_FINGER_TIP]
            MiddleCoordinatesLandmark = mp_drawing._normalized_to_pixel_coordinates(MiddleLandmark.x, MiddleLandmark.y, frameWidth, frameHeight)

            RingLandmark = results.multi_hand_landmarks[0].landmark[mp_hands.HandLandmark.RING_FINGER_TIP]
            RingCoordinatesLandmark = mp_drawing._normalized_to_pixel_coordinates(RingLandmark.x, RingLandmark.y, frameWidth, frameHeight)

            ThumbLandmark = results.multi_hand_landmarks[0].landmark[mp_hands.HandLandmark.THUMB_TIP]
            ThumbCoordinatesLandmark = mp_drawing._normalized_to_pixel_coordinates(ThumbLandmark.x, ThumbLandmark.y, frameWidth, frameHeight)
            
                # defining instance of class node
            Index =  node(is_index , (IndexCoordinatesLandmark[0] , IndexCoordinatesLandmark[1]))
            Middle =  node(is_middle , (MiddleCoordinatesLandmark[0] , MiddleCoordinatesLandmark[1]))
            Ring = node(is_ring , (RingCoordinatesLandmark[0] , RingCoordinatesLandmark[1]))
            Thumb = node(is_thumb , (ThumbCoordinatesLandmark[0] , ThumbCoordinatesLandmark[1]))

            Index.play()
            is_index = Index.is_playing

            Middle.play()
            is_middle = Middle.is_playing

            Ring.play()
            is_ring = Ring.is_playing

            Thumb.play()
            is_thumb = Thumb.is_playing
                



            
            # print(f" {IndexCoordinatesLandmark[0]},{IndexCoordinatesLandmark[1]}  {'/'} {MiddleCoordinatesLandmark[0]},{MiddleCoordinatesLandmark[1]} {'/'} {RingCoordinatesLandmark[0]},{RingCoordinatesLandmark[1]} {'/'} {ThumbCoordinatesLandmark[0]},{ThumbCoordinatesLandmark[1]} ")  

        # if results.left_hand_landmarks:
        #     for hand_landmarks in results.left_hand_landmarks.landmark:
        #         mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
        #         keypoint_pos = []
        #         for i in range(21):
        #             x = hand_landmarks.landmark[i].x * frame.shape[1]
        #             y = hand_landmarks.landmark[i].y * frame.shape[0]
        #             keypoint_pos.append((x, y))


        
             
        cv2.imshow('Hand Tracking', image)

        if cv2.waitKey(10) & 0xFF == ord('q'):
            break
cap.release()
cv2.destroyAllWindows()

# os.mkdir('Output Images')

# cap = cv2.VideoCapture(0)





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