import cv2


# Create our body classifier
body_classifier= cv2.CascadeClassifier('haarcasade_fullbody.xml')

# Initiate video capture for video file
cap = cv2.VideoCapture('walking.avi')

# Loop once video is successfully loaded
while True:
     # Read first frame
    ret, frame = cap.read()

    #Convert Each Frame into Grayscale
    faces(gray) = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    
    # Pass frame to our body classifier
    bodies = body_classifier.detectMultiScale(gray, 1.2,3)
    
   for (x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h), (250,0,0),2)
    

    if cv2.waitKey(1) == 32: #32 is the Space Key
        break

cap.release()
cv2.destroyAllWindows()
