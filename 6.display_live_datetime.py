import cv2
from datetime import datetime
 
# Open video
cap = cv2.VideoCapture("sample.mp4")
 
while True:
    ret, frame = cap.read()
 
    if not ret:
        break
 
    # Get current date and time
    current_time = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
 
    # Display date and time on the video
    cv2.putText(frame, current_time, (20, 30),
                cv2.FONT_HERSHEY_SIMPLEX, 0.8,
                (0, 255, 0), 2)
 
    cv2.imshow("Video with Date and Time", frame)
 
    if cv2.waitKey(30) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()