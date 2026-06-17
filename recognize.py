import cv2
from datetime import datetime

Face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades +
    "haarcascade_frontalface_default.xml"
)

cap = cv2.VideoCapture(0)

name = ()

recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read("trainer.yml")

attendance_marked = set()

while True:
    ret, frame = cap.read()

    if not ret:
        print("Unable to load Camera!")
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = Face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30)
    )
    for (x, y, w, h) in faces:
        face = gray[y:y+h, x:x+w]

        label, confidence = recognizer.predict(face)
   
        names = {
            0: "Bhagyashri"
        }
    
        name = names[label]
    
    if name not in attendance_marked:
        attendance_marked.add(name)
        
        now = datetime.now()
        date = now.strftime("%Y-%m-%d")
        time = now.strftime("%H:%M:%S")
    
    for (x, y, w, h) in faces:
        cv2.rectangle(
            frame,
            (x, y),
            (x + w, y + h),
            (0, 255, 0),
            2
        )
        cv2.putText(frame, f"{name} Present, Time = {time}, Date= {date}",(x, y - 10), cv2.FONT_HERSHEY_PLAIN, 1.1,(0, 255, 0) ,2)
        
        cv2.imshow("Face Recognizer", frame)
    
        
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
