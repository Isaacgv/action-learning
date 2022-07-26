from pickle import TRUE
import cv2
import sys
import time


video_path = sys.argv[1]
TIMER = int(3)

cap= cv2.VideoCapture(0)

width= int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height= int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

writer= cv2.VideoWriter(video_path, cv2.VideoWriter_fourcc(*'DIVX'), 20, (width,height))
font = cv2.FONT_HERSHEY_SIMPLEX
        
while True :

    ret,frame= cap.read()       
    frame=cv2.flip(frame,1)
    cv2.imshow('frame', frame)           

    k = cv2.waitKey(1)
    
    if k == ord('s'):
        prev = time.time()

        while TIMER >= 0:
            ret, frame = cap.read()

            # Display countdown on each frame
            # specify the font and draw the
            # countdown using puttext
         
            text = str(TIMER)

            # get boundary of this text
            textsize = cv2.getTextSize(text, font, 1, 2)[0]

            # get coords based on boundary
            textX = (frame.shape[1] - textsize[0]) / 2
            textY = (frame.shape[0] + textsize[1]) / 2
            
            frame=cv2.flip(frame,1)
            cv2.putText(frame, text, (int(textX), int(textY)),
                        font, 5, (0, 0, 255), 5, cv2.LINE_AA)
     
            cv2.imshow('frame', frame)
            
            cv2.waitKey(1)

            # current time
            cur = time.time()
            
            if cur-prev >= 1:
                prev = cur
                TIMER = TIMER-1
    elif TIMER < 0:
        writer.write(frame)

        # Update and keep track of Countdown
        # if time elapsed is one second
        # than decrease the counter

    if k== ord('q'):
            break

cap.release()
writer.release()
cv2.destroyAllWindows()

if TIMER>0:
    sys.exit(0)
else:
    sys.exit(2)

