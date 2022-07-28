
from ast import IsNot
import os
import cv2
from git import safe_decode
import numpy as np
#import av
import mediapipe as mp
import streamlit as st
import mediapipe as mp
import subprocess
from os.path import exists
import uuid 


import sys
sys.path.append("..")


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
def sign_recognition_video():
    new_title = '<p style="font-size: 42px; font-weight:bolder;">Sign Language Recognition for &#127909;<br/></p>'
    st.markdown(new_title, unsafe_allow_html=True)
    st.markdown("""<p style="font-size: 25px; font-weight:bolder;">
    This Sign Language Detection Model takes in a video as an input and then outputs that video """ +
    """along side the sign word equivalant in natutral Langauge</br></br> &#129330; &#10133; &#129302; &#10145; Thank you !</p></br>""", unsafe_allow_html=True)
  
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
                process =subprocess.run(["python", "mediapipe/utils/test.py",os.path.join("videos/keepers",file.name)])
                
            
    st.markdown("<hr style= size='6', color=black> ", unsafe_allow_html=True)
    st.subheader("Option 2 - Redcord using Webcam")
    st.markdown("<p style='font-size: 20px' ><b>Instructions</b><ul><li>Press ( S ) to Start</li><li>Wait the timer for 3 Seconds</li><li>Press ( Q ) to Quit</p> ", unsafe_allow_html=True)
    
    
    run =st.button("Launch Webcam")
    file_code =str(uuid.uuid4())[:8]
    path ="videos/keepers/"+file_code+".mp4"
    
    showthem =False
    if run:
        process =subprocess.run(["python", "camera.py",path])
       
        print(path)
        if process.returncode ==0:
            st.write("Nothing Was Redorded!")
        
        elif exists(path):
            st.write("Video Was Redorded!")
            st.video(path)
            process =subprocess.run(["python", "mediapipe/utils/test.py",'videos/keepers/'+file_code+'.mp4',file_code])
            keep =st.checkbox("Keep Video")
            delete=st.checkbox("Delete Video")
            time.sleep(1)
            f = open("temp/result.txt","r")
            x = (f.read())
            
            st.video("videos/inference/"+file_code+".mp4")
           
            if keep:
                
                st.write("Video Was Submited Sucessefully!!")
                return file_code
            
            elif delete:
                 pass
        
# def sign_recognition_image(): 
#     new_title = '<p style="font-size: 42px; font-weight:bolder;">Sign Language Recognition for &#127878;<br/></p>'
#     st.markdown(new_title, unsafe_allow_html=True)
#     st.markdown("""<p style="font-size: 25px; font-weight:bolder;">
#     This Sign Language Detection Model takes in an image as an input and then outputs that image with bounding boxes """ +
#     """describing the ASL equivalant word in natutral Langauge</br></br> &#128075; &#10133; &#129302; &#10145; Hello!</p></br>""", unsafe_allow_html=True)
  
#     file = st.file_uploader('', type = ['jpg','png','jpeg'])
#     if file is not None:
#         st.image(file)
#         save =st.button("Save Image")  
#         if save: 
#             with open(os.path.join("images",file.name),"wb") as f: 
#                 f.write(file.getbuffer())         
#                 st.success("Saved File")

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
    choice  = st.sidebar.selectbox("MODE",("About","Sign Language Recognition(Video)","Docs")) # "Sign Language Recognition(Image)",
    #["Show Instruction","Landmark identification","Show the #source code", "About"]
    
    # if choice == "Sign Language Recognition(Image)":
    #     read_me_0.empty()
    #     read_me.empty()
    #     read_repo.empty()
    #     sign_recognition_image()
        
    if choice == "Sign Language Recognition(Video)":
        read_me_0.empty()
        read_me.empty()
        read_repo.empty()
        file_code =sign_recognition_video()
    elif choice == "About":
        print()
    elif choice=="Docs":
        st.markdown(""" ## User Guide: :clipboard:

* Using our application you will be able to detect, translate sign language into natural words
* Create/use your own sign language too ! 
* This application is for educational purposes and anyone who wants to discover and learn
  sign language

P.S We are using American Sign Language (ASL) you can find more details here
 [ASL](https://www.signingsavvy.com/)

## Features:
##### Detecting Sign Language :
 There are two ways you can detect sign language:
 * Click on Sign Language Recognition(Video)

##### Option 1
 * Upload videos from your file 
""")
        image = Image.open("doc_img/upload.png")
        st.image(image)

        st.markdown(""" * After upload a video you can replay, save it or use another one """)
        image = Image.open("doc_img/save_vid.png")
        st.image(image)

        st.markdown(""" 
        * When clicking on save the detection of the sign language will be displayed, a video a long with the word. Try it !!
        """)

        st.markdown("##### Option 2")
        st.markdown(""" 
        * You can record a video yourself on our website 
        * Click on the Launch Webcam button to open the webcam
        *  Press on S to start the countdown 
        *  Press on Q to stop the recording 
        *  You can either record another video or save it
                        """)
        image_1 = Image.open("doc_img/webc.png")
        st.image(image_1)
        image = Image.open("doc_img/counter.png")
        st.image(image)

        

if __name__ == '__main__':
		main()	