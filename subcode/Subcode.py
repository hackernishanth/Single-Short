import face_recognition
import numpy as np
import cv2

# Mean Squared Error 
def MeanQuareError(FirstImage, SecondImage):

	# sum of the squared difference between the two images;
	# NOTE: the two images must have the same dimension
        # Finding the error similarity between two images
	error = np.sum((FirstImage.astype("float") - SecondImage.astype("float")) ** 2)
	return error / float(FirstImage.shape[0] * FirstImage.shape[1])
    
def imageCapture(frame):
    try:
        # storing the face location
        face_locations = []
        small_frame = cv2.resize(frame, (0,0), fx=0.5, fy= 0.5)    
        rgb_small_frame = small_frame[:,:,::-1]
        
        # Face Detection using SSD Model
        face_locations = face_recognition.face_locations(rgb_small_frame, number_of_times_to_upsample=2)
        
        # Drawing the face bounding box's using the face location 
        for (top,right,bottom,left) in face_locations:
            top = top * 2
            right = right * 2
            bottom = bottom * 2
            left = left * 2
            cv2.rectangle(frame, (left,top),(right,bottom), (0,0,255), 2)
        
        # Plotting the box for verifying the ID card
        cv2.rectangle(frame, (300, 250), (20, 70), (0,255,0), 2)

        # cropping the ID Card from the Current frame
        IdCroppedFromFrame = frame[70:250,20:300]
        id_cropped_resized = cv2.resize(IdCroppedFromFrame,(500,500))

        # face location, Frame, Croped ID card as the return responce 
        # if len(face_locations) == 2:
        return face_locations, frame, id_cropped_resized
    except:
        print("No Face Identified in the image")
    


# similarity between Two Images
def similarityChecker(FirstEncodedImage,SecondEncodedImage):

    # Using Dlib we are Finding the distance similarity
    FeatureDistance = face_recognition.face_distance(np.array(FirstEncodedImage),np.array(SecondEncodedImage))   
    # print(distance)
    
    # distance is indirectly propotional to the Accuracy
    if(FeatureDistance<0.45): # 0.45 is the thershold value
        
        # Face Verifiaction Failed
        return True
    
    else:

        # Face Verifiaction Failed
        return False 

# check if Id card is valid
def idChecker(imageToVerify):
    
    isValid = False

    # we are reshaping the Image to find similarity
    imageToVerify_resized = cv2.resize(imageToVerify, (500,500))

    # Loading the Imagess for verify if it is Aadhar Card, Driving licence (Or) Pan Card
    PanCard = cv2.imread("./VerificationDataset/PanCard.jpeg")
    AadhaarCard = cv2.imread("./VerificationDataset/AadhaarCard.jpg")
    DrivingLicense = cv2.imread("./VerificationDataset/DrivingLicence.jpeg")
    
    # resizing the ID Card for Compare if it is Aadhar Card, Driving licence (Or) Pan Card
    DrivingLicense = cv2.resize(DrivingLicense,(500,500))
    AadhaarCard = cv2.resize(AadhaarCard,(500,500))    
    PanCard = cv2.resize(PanCard,(500,500))

    # Verifying if ID Card is accepted
    for ThingsInList in [DrivingLicense, AadhaarCard, PanCard]:

        # Comparing the two images
        # error is indirectly proportional to the Accuracy
        ErrorDifference = (MeanQuareError(ThingsInList, imageToVerify_resized))
        # print(score)

        # Score is indirectly propotional to the Accuracy
        if (ErrorDifference < 14000): # 14000 is the thershold range
            isValid = True 
            break

    return isValid

# Verification for IDCard and Two face's
def verification(coords):

    # Loading the Detected Id Card
    idImg = cv2.imread('./TestedSamples/Croped ID Card.PNG')

    # ID Card Verification
    if(idChecker(idImg)):
        
        # Face Verification
        img = cv2.imread('./TestedSamples/Image.PNG')

        # encoding the Face using Resnet
        # Extracting the feature from the First and Second Image
        FeatureOne = face_recognition.face_encodings(img, [coords[0]])
        Featuretwo = face_recognition.face_encodings(img, [coords[1]])

        # Calling the similarityChecker function and sending the return responce as boolean
        return(similarityChecker(FeatureOne, Featuretwo))
    else:

        # Id Card Verification Failed
        return False 




