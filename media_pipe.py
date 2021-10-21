from typing import Counter
import cv2 as cv
import mediapipe as mp
import numpy as np
#import time

mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose

count = 0
state = None

cap = cv.VideoCapture(0)
## Setup mediapipe instance
with mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5) as pose:
    while cap.isOpened():
        ret, frame = cap.read()
        
        # Recolor image to RGB
        image = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
        image.flags.writeable = False
      
        # Make detection
        results = pose.process(image)
    
        # Recolor back to BGR
        image.flags.writeable = True
        image = cv.cvtColor(image, cv.COLOR_RGB2BGR)
        
        # Extract landmarks
        try:
            landmarks = results.pose_landmarks.landmark

            # got the co-ordinates of shoulder and knee
            shoulder = [landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].x,landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].y]
            knee= [landmarks[mp_pose.PoseLandmark.LEFT_KNEE.value].x,landmarks[mp_pose.PoseLandmark.LEFT_KNEE.value].y]
            

            #calculate the distance between these co-ordinates

            a = np.array(shoulder)
            b = np.array(knee)

            distance = np.linalg.norm(a-b)
            #print(f'The distance is: {distance}')

            if distance < 0.31:
                state = "Down"
            
            if 0.6<distance< 0.65 and state == "Down":
                state = "Up"
                count+=1

        except:
            pass
        
        #set up box in image frame to show the squats done

        cv.rectangle(image, (0,0), (200,60), (0,0,0) , -1)

        #suaqt data display

        cv.putText(image, 'Squats', (10,10), cv.FONT_HERSHEY_PLAIN, 1, (255,255,255), 1 , cv.LINE_AA)

        cv.putText(image, str(count), (10,20), cv.FONT_HERSHEY_PLAIN, 1, (255,255,255), 1 , cv.LINE_AA)

        #position/state of yours

        cv.putText(image, "State/Position" , (10,40), cv.FONT_HERSHEY_COMPLEX_SMALL, 0.4, (255,255,255), 1 , cv.LINE_AA)
        cv.putText(image, state, (10,50), cv.FONT_HERSHEY_COMPLEX_SMALL, 0.4, (255,255,255), 1, cv.LINE_AA)


        # Render detections
        mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS,
                                mp_drawing.DrawingSpec(color=(0,0,255), thickness=2, circle_radius=2), 
                                mp_drawing.DrawingSpec(color=(0,255,0), thickness=2, circle_radius=2) 
                                 )               
        
        cv.imshow('Mediapipe Feed', image)

        

        if cv.waitKey(10) & 0xFF == ord('q'):
            break

    cap.release()
    cv.destroyAllWindows()