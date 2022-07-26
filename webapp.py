from pickle import FRAME
import cv2
import numpy as np
import av
import mediapipe as mp
import streamlit as st
import mediapipe as mp

# Live Camera Stream

# mp_drawing = mp.solutions.drawing_utils
# mp_drawing_styles = mp.solutions.drawing_styles
# mp_hands = mp.solutions.hands
# hands = mp_hands.Hands(
#     model_complexity=0,
#     min_detection_confidence=0.5,
#     min_tracking_confidence=0.5
# )

# def process(image):
#     image.flags.writeable = False
#     image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
#     results = hands.process(image)
# # Draw the hand annotations on the image.
#     image.flags.writeable = True
#     image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
#     if results.multi_hand_landmarks:
#       for hand_landmarks in results.multi_hand_landmarks:
#         mp_drawing.draw_landmarks(
#             image,
#             hand_landmarks,
#             mp_hands.HAND_CONNECTIONS,
#             mp_drawing_styles.get_default_hand_landmarks_style(),
#             mp_drawing_styles.get_default_hand_connections_style())
#     return cv2.flip(image, 1)

# RTC_CONFIGURATION = RTCConfiguration(
#     {"iceServers": [{"urls": ["stun:stun.l.google.com:19302"]}]}
# )
# webrtc_ctx = webrtc_streamer(
#     key="TEST",
#     mode=WebRtcMode.SENDRECV,
#     rtc_configuration=RTC_CONFIGURATION,
#     media_stream_constraints={"video": True, "audio": False},
#     async_processing=True,
# )

# class VideoProcessor:
#     def recv(self, frame):
#         img = frame.to_ndarray(format="bgr24")
#         img = process(img)
#         return av.VideoFrame.from_ndarray(img, format="bgr24")
    
# webrtc_ctx = webrtc_streamer(
#     key="WYH",
#     mode=WebRtcMode.SENDRECV,
#     rtc_configuration=RTC_CONFIGURATION,
#     media_stream_constraints={"video": True, "audio": False},
#     video_processor_factory=VideoProcessor,
#     async_processing=True,
# )

def object_detection_video():
    st.title("Sign Language Recognition for Videos")
    st.subheader("""
    This object detection project takes in a video and outputs the video with bounding boxes created around the objects in the video 
    """
    )
    st.title("Webcam Live Feed")
    frameWidth = 640
    frameHeight = 480
    cap = cv2.VideoCapture(-1,cv2.CAP_DSHOW)
    cap.set(3, frameWidth)
    cap.set(4, frameHeight)
    cap.set(10,150)
    while cap.isOpened():
        success, img = cap.read()
        if success:
            cv2.imshow("Result", img)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        
    
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