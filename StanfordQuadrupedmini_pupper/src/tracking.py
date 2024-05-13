# import the opencv library 
import cv2 
  
  
# Define the GStreamer pipeline string
pipeline_string = 'videofilesrc location=./modules/videoio/src/cap_gstreamer.cpp ! decodebin ! videoconvert ! videoscale'

# Create a VideoCapture object with the GStreamer pipeline
cap = cv2.VideoCapture(pipeline_string, cv2.CAP_GSTREAMER)
  
while(True): 
      
    # Capture the video frame 
    # by frame 
    ret, frame = cap.read() 
  
    # Display the resulting frame 
    cv2.imshow('frame', frame) 
      
    # the 'q' button is set as the 
    # quitting button you may use any 
    # desired button of your choice 
    if cv2.waitKey(1) & 0xFF == ord('q'): 
        break
  
# After the loop release the cap object 
cap.release() 
# Destroy all the windows 
cv2.destroyAllWindows() 