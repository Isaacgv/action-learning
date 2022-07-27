

import cv2
import os
import sys
import time
path_to_video = "data/thumbs_up.mp4"
cap = cv2.VideoCapture(path_to_video)
frameNr = 0
frame_rate = 30
labels = "thumbs_up"
path = labels 
prev = 0

fps = cap.get(cv2.CAP_PROP_FPS)
print(fps)
while (True):
    
    success, frame = cap.read()
    frame = cv2.flip(frame,0)
    
    if frame is not None:
        if os.path.exists(labels):
        
            cv2.imwrite(f'{path}/images/{frameNr}.jpg', frame)
        else:
            print("t")
            os.system("mkdir "+labels)
            os.system("cd "+labels+"&& mkdir images")
            cv2.imwrite(f'{path}/images/{frameNr}.jpg', frame)

        frameNr = frameNr+1
        cv2.waitKey(1000)
    else:
        break
os.system("cp "+path_to_video+" " + labels+"/"+labels+".mp4")
cap.release()
cv2.destroyAllWindows()







