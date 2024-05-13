import cv2

def main():
    # Create a VideoCapture object to capture video from the webcam
    cap = cv2.VideoCapture(0)  # 0 is the default camera, change it if you have multiple cameras
    
    # Loop to continuously capture frames from the webcam
    while True:
        # Read a frame from the webcam
        ret, frame = cap.read()
        
        # Check if the frame was read successfully
        if not ret:
            print("Error: Failed to read frame.")
            break
        
        # Display the captured frame
        cv2.imshow("Webcam", frame)
        
        # Check for the 'q' key to exit the loop
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    # Release the VideoCapture object and close all OpenCV windows
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()