import cv2
 
# Open video
cap = cv2.VideoCapture("sample1.mp4")
 
# Read first frame
ret, frame = cap.read()
 
if not ret:
    print("Unable to read video.")
    exit()
 
# Create CSRT tracker
tracker = cv2.TrackerCSRT_create()
 
# Select object manually
bbox = cv2.selectROI("Select Object", frame, False)
 
# Initialize tracker
tracker.init(frame, bbox)
 
while True:
    ret, frame = cap.read()
 
    if not ret:
        break
 
    success, bbox = tracker.update(frame)
 
    if success:
        x, y, w, h = [int(v) for v in bbox]
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.putText(frame, "Tracking", (20, 30),
                    cv2.FONT_HERSHEY_SIMPLEX, 1,
                    (255, 0, 0), 2)
    else:
        cv2.putText(frame, "Tracking Failed", (20, 30),
                    cv2.FONT_HERSHEY_SIMPLEX, 1,
                    (0, 0, 255), 2)
 
    cv2.imshow("Object Tracking", frame)
 
    if cv2.waitKey(30) & 0xFF == ord('q'):
        break
 
cap.release()
cv2.destroyAllWindows()