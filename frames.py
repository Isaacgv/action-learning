

import cv2
import os
import sys
import time
import sys 

video_path = sys.argv[1]
labels = sys.argv[2]
path_to_video = video_path
cap = cv2.VideoCapture(path_to_video)
frameNr = 0
frame_rate = 30

path = labels 
prev = 0

fps = cap.get(cv2.CAP_PROP_FPS)
while (True):
    
    success, frame = cap.read()
    if frame is not None:
        if os.path.exists(labels):
        
            cv2.imwrite(f'{path}/images/{frameNr}.jpg', frame)
        else:
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







