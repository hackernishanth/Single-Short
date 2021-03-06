# Single Short Image Classification

<p align="center">
<a href="#">
         <img alt="Qries" src="https://dvqlxo2m2q99q.cloudfront.net/000_clients/222003/page/222003kxyukmaX.gif"
          width="100%" height="100%">
      </a>

---

## Table of Contents

- [Description](#description)
- [Quick start](#quick-start)
- [Increase Model Performance](#Increase-Model-Performance)
- [Help](#help)

---

## Description

When the user runs the application, the camera should be turned on and it should capture the live image of the user using the front camera in the system.
The user should hold any one of the following ID cards near their face while appearing for the selfie (Quality must be clear and readable with no obstruction of fingers,
out-of-frame cuts or blurred pixels.) Halleyx Confidential. For office use only. 

Acceptable ID forms
- Driver’s Licence
- Passport
- Aadhar card
- PAN card

When the user clicks on the “Verify” button, and if both the selfie picture as well as the image in the document matches, a “Success” message should be displayed. Else, it should display a “Failure” message.

---

## Quick start

```html
https://github.com/hackernishanth/Single-Short.git
cd Single Short
```

### To create a [virtual environments](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

## To install and create
```html
On Windows...
   ==> py -m pip install --user virtualenv
   ==> py -m venv env

On macOS and Linux...
   ==> python3 -m pip install --user virtualenv
   ==> python3 -m venv env
```

## To run the Model
```html
pip install -r requirements.txt
python main.py
```
---

## Test Result

<p align="center">
<a href="#">
         <img src="https://raw.githubusercontent.com/hackernishanth/Single-Short/main/TestedSamples/Landing%20Page.PNG"
         width="400" height="400">
      </a>   
<a href="#">
         <img src="https://raw.githubusercontent.com/hackernishanth/Single-Short/main/TestedSamples/success%20Landing.PNG"
         width="400" height="400">
      </a>  
<a href="#">
         <img src="https://raw.githubusercontent.com/hackernishanth/Single-Short/main/TestedSamples/Invalid.PNG"
         width="400" height="400">
      </a>   
<a href="#">
         <img src="https://raw.githubusercontent.com/hackernishanth/Single-Short/main/TestedSamples/Failed%20Landing.PNG"
         width="400" height="400">
      </a>   
         
---

## Increase Model Performance
Instead of SSD Resnet model Replace You Only Look Once(yolo) Object Detection model
- [yolov4](https://github.com/Tianxiaomo/pytorch-YOLOv4)
- [Image Processing](https://github.com/ageitgey/face_recognition/blob/master/examples/digital_makeup.py)

---

## Help

- use issues.txt file for solving Package error
