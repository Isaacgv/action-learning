from turtle import width
import streamlit as st
import subprocess
import os
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
    """along side the sign word equivalant in natutral Langauge</br></br> &#129330; &#10133; &#129302; &#10145;"""+
    """ Thank you !</p></br>""", unsafe_allow_html=True)
  
    st.subheader("Option 1 - Upload a video")
    file = st.file_uploader('', type = ['mp4'])
  
    if file is not None:
        file_path= os.path.join("videos/keepers",file.name)
        st.video(file)
        save =st.button("Save Video")  
        if save: 
            with open(file_path,"wb") as f: 
                f.write(file.getbuffer())         
                st.success("Saved File")
                process =subprocess.run(["python", "mediapipe/utils/test.py",os.path.join("videos/keepers",file.name)])
                

    st.markdown("<hr style= size='6', color=black> ", unsafe_allow_html=True)
    st.subheader("Option 2 - Redcord using Webcam")
    st.markdown("<p style='font-size: 20px' ><b>Instructions</b><ul><li>Press ( S ) to Start</li><li>Wait the "+
                "timer for 3 Seconds</li><li>Press ( Q ) to Quit</p> ", unsafe_allow_html=True)
    
    
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
            process =subprocess.run(["python", "mediapipe/utils/test.py",'videos/keepers/'+file_code+'.mp4'])
            keep =st.checkbox("Keep Video")
            delete=st.checkbox("Delete Video")
            if keep:
                st.write("Video Was Submited Sucessefully!!")
                return file_code
            elif delete:
                 pass

def sign_recognition_Video_retraining():
    new_title = '<p style="font-size: 42px; font-weight:bolder;">Teach me a Sign &#x1F468;<br/></p>'
    st.markdown(new_title, unsafe_allow_html=True)
    st.markdown("""<p style="font-size: 25px; font-weight:bolder;">
    This Sign Language Detection Model can learn a new Sign Langauge gesture only from taking a video as an input from the user """ +
    """</br></br> &#127909; &#10133; &#129302; &#129305;"""+
    """ Thank you !</p></br>""", unsafe_allow_html=True)
  
    st.subheader("Redcord using Webcam")
    st.markdown("<p style='font-size: 20px' ><b>Instructions</b><ul><li>Press ( S ) to Start</li><li>Wait the "+
                "timer for 3 Seconds</li><li>Press ( Q ) to Quit</p> ", unsafe_allow_html=True)
    
    col1, col2, col3= st.columns(3)
    with col1:
        title = st.text_input('Give your Sign a Name', 'Name goes here')
        
    run =st.button("Launch Webcam")
    file_code =title.strip()
    path ="videos/keepers/"+file_code+".mp4"
    
    if run:
        if len(title) ==0 :
            st.error("Please Enter a Sign Name")
        elif title == "Name goes here":
            st.error("Please Enter a valid Sign Name")
        elif len(title) > 15 :
            st.error("You can't use more than 10 characters")
        else:
            process_training =subprocess.run(["python", "camera.py",path])
            print(path)
            if process_training.returncode ==0:
                st.write("Nothing Was Redorded!")
            
            elif exists(path):
                st.write("Video Was Redorded!")
                st.video(path)
            
                st.write('Name your Sign Language', title)
                process_training =subprocess.run(["python", "frames.py",'videos/keepers/'+file_code+'.mp4',title])
                keep =st.checkbox("Keep Video")
                delete=st.checkbox("Delete Video")
                if keep:
                    st.write("Video Was Submited Sucessefully!!")
                    return file_code
                elif delete:
                    pass
    
def main():
    new_title = '<p style="font-size: 42px; font-weight:bolder;">SignMe &#128406;<br/></p><p style="font-size: 32px;">Welcome to our App!</p>'
    read_me_0 = st.markdown(new_title, unsafe_allow_html=True)

    read_me = st.markdown("""<p style="font-size: 24px;text-align: left;">
    This research project is built to demonstrate the importance of <b>Few Shot Learning in Sign Language Recognition</b>.
    It was built using Streamlit and Mediapipe and many more computer vision Libraries.""",unsafe_allow_html=True)
    img_0=st.image("images/signme.png", width=660)
    line_0=st.markdown("<hr style= size='6', color=black> ", unsafe_allow_html=True)
    img_1=st.image("images/github.png", width=50)
    read_repo = st.markdown("""Our Github repository can be found 
    [here](https://github.com/Isaacgv/action-learning/tree/main)""")
    
    st.sidebar.title("Select Activity")
    choice  = st.sidebar.selectbox("MODE",("About","Instructions","Sign Language Recognition", "Teach me a Sign")) # "Sign Language Recognition(Image)",
    #["Show Instruction","Landmark identification","Show the #source code", "About"]
    if choice == "About":
        print()
    if choice == "Sign Language Recognition":
        img_0.empty()   
        img_1.empty()  
        line_0.empty() 
        read_me_0.empty()
        read_me.empty()
        read_repo.empty()
        
        file_code =sign_recognition_video()
        
    elif choice == "Teach me a Sign":
        img_0.empty()   
        img_1.empty()  
        line_0.empty() 
        read_me_0.empty()
        read_me.empty()
        read_repo.empty()
   
        sign_recognition_Video_retraining()
        

if __name__ == '__main__':
		main()	