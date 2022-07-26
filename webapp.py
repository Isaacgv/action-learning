
import os
import cv2
import numpy as np
import av
import mediapipe as mp
import streamlit as st
import mediapipe as mp
import subprocess
from os.path import exists
import web_services as sv
import uuid 
  

# Live Camera Stream

def object_detection_video():
    st.title("Sign Language Recognition for Videos")
    st.subheader("""
    This object detection project takes in a video and outputs the video with bounding boxes created around the objects in the video 
    """
    )
    st.title("Redcord using Webcam")
    run =st.button("Launch Webcam")
    file_code = str(uuid.uuid4())[:10]
    path ="videos/"+file_code+".mp4"
    showthem =False
    if run:
        process =subprocess.run(["python", "camera.py",path])
        if process.returncode ==0:
            st.write("Nothing Was Redorded!")
        elif exists(path):
            st.write("Video Was Redorded!")
            st.video(path)
            showthem=True
    if showthem : 
        keep =st.button("Keep it"),
        tryAgain =st.button("Try again")
        
        if keep:
            st.write("Video Was Submited Sucessefully!!")  
        elif tryAgain:
                pass
                        
    
def object_detection_image(): 
    st.title('Sign Language Recognition for Images')
    st.subheader("""
    This project takes in an image and outputs the image with bounding boxes created around the objects in the image showing the sign language detected in the image.
    """)
    file = st.file_uploader('Upload Image', type = ['jpg','png','jpeg'])


def main():
    new_title = '<p style="font-size: 42px; font-weight:bolder;">SignMe &#128406;<br/></p><p style="font-size: 38px;">Welcome to our App!</p>'
    read_me_0 = st.markdown(new_title, unsafe_allow_html=True)

    read_me = st.markdown("""<p style="font-size: 26px;text-align: left;">
    This research project is built to demonstrate the importance of <b>Few Shot Learning in Sign Language Recognition</b>.
    It was built using Streamlit and Mediapipe and many more computer vision Libraries.
    in both videos(pre-recorded)
    and images.""",unsafe_allow_html=True)
    
    read_repo = st.markdown("""
     The Github repository can be found 
    [here](https://github.com/Isaacgv/action-learning/tree/main)""")
    st.sidebar.title("Select Activity")
    choice  = st.sidebar.selectbox("MODE",("About","Sign Language Recognition(Image)","Sign Language Recognition(Video)"))
    #["Show Instruction","Landmark identification","Show the #source code", "About"]
    
    if choice == "Sign Language Recognition(Image)":
        read_me_0.empty()
        read_me.empty()
        read_repo.empty()

        object_detection_image()
        
    elif choice == "Sign Language Recognition(Video)":
        read_me_0.empty()
        read_me.empty()
        read_repo.empty()
        object_detection_video()
        #if object_detection_video.has_beenCalled:
        # try:

        #     clip = moviepy.VideoFileClip('detected_video.mp4')
        #     clip.write_videofile("myvideo.mp4")
        #     st_video = open('myvideo.mp4','rb')
        #     video_bytes = st_video.read()
        #     st.video(video_bytes)
        #     st.write("Detected Video") 
        # except OSError:
        #     ''

    elif choice == "About":
        print()
        

if __name__ == '__main__':
		main()	