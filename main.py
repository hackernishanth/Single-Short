# Required Packages
import cv2
import webbrowser
from subcode.Subcode import *
from flask import Flask, render_template, Response, request, jsonify, redirect, url_for

# calling the Flask class
app = Flask('templates')

"""
Access the First webcam  feed using ==> '0'
Access the Second webcam feed using ==> '1'
Access the CCTV camera video feed using ==> 'rtsp://<username>:<password>@IPAddress' 
"""
camera = cv2.VideoCapture(1)

# Generating the frames
def gen_frames():  
    while True:
        success, frame = camera.read()  # read the camera frame

        # Finding the Faces in the frame 
        coords, out_frame, id_cropped_resized = imageCapture(frame)
        
        # Check if frame is empty
        if not success:
            break
        else:            
            # convering the frames to encoding formate
            ret, buffer = cv2.imencode('.jpg', out_frame)

            # converting the buffer to bytes
            frame = buffer.tobytes()

            # yeild will the frame from backend to frontend
            yield (b'--frame\r\n'b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/')
def index():

    # render the Home Landing page
    return render_template('index.html')

@app.route('/NotVerifyed')
def NotVerifyed():

    # Render when the authentication Failed
    return render_template('NotVerifyed.html')  

@app.route('/Verifyed')
def Verifyed():
    
    # Render when the authentication Failed
    return render_template('Verifyed.html')  

# saving the current frame
@app.route('/CaptureCurrentFrame', methods = ['POST'])
def CaptureCurrentFrame():

    # read the camera frame
    _, frame = camera.read() 

    # Saving the current frame present in the screen when the button is pressed
    coords, out_frame, id_cropped_resized = imageCapture(frame)

    # Saving the User/Client Face Image
    cv2.imwrite('./TestedSamples/Image.PNG', out_frame)

    # Saving the ID card Face Image
    cv2.imwrite('./TestedSamples/Croped ID Card.PNG', id_cropped_resized)

    # Face verification blog
    if(verification(coords)):
        
        # Returning the responce as success
        return "http://127.0.0.1:5000/Verifyed"
    
    else:

        # Returning the responce as Failed
        return "http://127.0.0.1:5000/NotVerifyed"

@app.route('/video_feed')
def video_feed():

    # the live feed can viewed in 'localhost:/video_feed' url
    return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')


if __name__ == '__main__':
    
    # opening the web browser automatically
    webbrowser.open('http://127.0.0.1:5000/')

    # Initializing the Flask Application 
    app.run(host="127.0.0.1",port=5000, debug=True)
    
