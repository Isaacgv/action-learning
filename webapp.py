
from ast import IsNot
import os
import cv2
from git import safe_decode
import numpy as np
import av
import mediapipe as mp
import streamlit as st
import mediapipe as mp
import subprocess
from os.path import exists
import uuid 
import shutil


### Styling the App
streamlit_style = """
			<style>
			@import url('https://fonts.googleapis.com/css?family=Open+Sans&display=swap');

			html, body, [class*="css"]  {
			font-family: 'Open Sans'
			}
			</style>
			"""
   
st.markdown(streamlit_style, unsafe_allow_html=True)
# Live Camera Stream



# functions for recording detection
def object_detection_video():
    new_title = '<p style="font-size: 42px; font-weight:bolder;">Sign Language Recognition for &#127909;<br/></p>'
    st.markdown(new_title, unsafe_allow_html=True)
    st.markdown("""<p style="font-size: 25px; font-weight:bolder;">
    This Sign Language Detection Model takes in a video as an input and then outputs that video with bounding boxes """ +
    """describing the ASL equivalant word in natutral Langauge</br></br> &#129330; &#10133; &#129302; &#10145; Thank you !</p></br>""", unsafe_allow_html=True)
  
    st.subheader("Option 1 - Upload a video")
    file = st.file_uploader('', type = ['mp4'])

    if file is not None:
        file_details = "File: Name: "+ str(file.name)+", Type: " +str(file.type)
        st.video(file)
        save =st.button("Save Video")  
        if save: 
            with open(os.path.join("videos/keepers",file.name),"wb") as f: 
                f.write(file.getbuffer())         
                st.success("Saved File")
            
            
    st.markdown("<hr style= size='6', color=black> ", unsafe_allow_html=True)
    st.subheader("Option 2 - Redcord using Webcam")
    st.markdown("<p style='font-size: 20px' ><b>Instructions</b><ul><li>Press ( S ) to Start</li><li>Wait the timer for 3 Seconds</li><li>Press ( Q ) to Quit</p> ", unsafe_allow_html=True)
    
    
    run =st.button("Launch Webcam")
    file_code = str(uuid.uuid4())[:8]
    path ="videos/keepers/"+file_code+".mp4"
    showthem =False
    if run:
        process =subprocess.run(["python", "camera.py",path])
        if process.returncode ==0:
            st.write("Nothing Was Redorded!")
        elif exists(path):
            st.write("Video Was Redorded!")
            st.video(path)
            keep =st.checkbox("Keep Video")
            delete=st.checkbox("Delete Video")
            if keep:
                st.write("Video Was Submited Sucessefully!!")
                return file_code
            elif delete:
                 pass
        
def object_detection_image(): 
    new_title = '<p style="font-size: 42px; font-weight:bolder;">Sign Language Recognition for &#127878;<br/></p>'
    st.markdown(new_title, unsafe_allow_html=True)
    st.markdown("""<p style="font-size: 25px; font-weight:bolder;">
    This Sign Language Detection Model takes in an image as an input and then outputs that image with bounding boxes """ +
    """describing the ASL equivalant word in natutral Langauge</br></br> &#128075; &#10133; &#129302; &#10145; Hellow !</p></br>""", unsafe_allow_html=True)
  
    file = st.file_uploader('', type = ['jpg','png','jpeg'])
    if file is not None:
        st.image(file)
        save =st.button("Save Image")  
        if save: 
            with open(os.path.join("images",file.name),"wb") as f: 
                f.write(file.getbuffer())         
                st.success("Saved File")

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
        file_code =object_detection_video()

    elif choice == "About":
        print()
        

if __name__ == '__main__':
		main()	