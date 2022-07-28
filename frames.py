import cv2
import os
import sys
import time
import sys 

def save_frames(label, path_to_video, video_time=3):
    cap = cv2.VideoCapture(path_to_video)
    user = path_to_video.split('/')[-1].split('.')[0]
    path = "training/" + label + "/" + user 
    fps = cap.get(cv2.CAP_PROP_FPS)
    length = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    capture_time = fps//video_time
    print(capture_time)
    count_frame = 0
    save_frame = 0

    while (True): 
        success, frame = cap.read()
        if frame is not None:
            count_frame = count_frame + 1
            if os.path.exists(path):
                print(count_frame, capture_time)
                if count_frame >= capture_time:
                    cv2.imwrite(f'{path}/images/{save_frame}.jpg', frame)
                    save_frame = save_frame + 1
                    count_frame = 0

            else:
                os.system("mkdir " + "/".join(path.split('/')[:2]))
                os.system("mkdir " + path)
                os.system("cd " + path + "&& mkdir images")
                cv2.imwrite(f'{path}/images/{save_frame}.jpg', frame)
                save_frame = save_frame + 1
            cv2.waitKey(1000)
        else:
            break

    os.system("cp "+ path_to_video + " " + path +"/"+label+".mp4")
    cap.release()

    cv2.destroyAllWindows()

def main():
    if len(sys.argv) > 0:
        path_to_video = sys.argv[1]
        label = sys.argv[2]
        save_frames(label, path_to_video)
        return 1
    else: 
        return 0
