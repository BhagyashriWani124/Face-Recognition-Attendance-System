import cv2
import os

# print(os.listdir("dataset"))
# print(cv2.__version__)
# print(hasattr(cv2, "face"))
name = input("Enter Name:")

Face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades +
    "haarcascade_frontalface_default.xml"
)

os.makedirs(f"dataset/{name}", exist_ok=True)
cap = cv2.VideoCapture(0)

count = 0

for i in range(1,51):
    ret, frame = cap.read()

    if ret:
        path = f"dataset/{name}/myphoto{i}.jpg"
        print(path)
        
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        
            
        faces = Face_cascade.detectMultiScale(
            gray,
            scaleFactor=1.1,
            minNeighbors=5
        )
            
        for (x, y, w, h) in faces:
            face = gray[y:y+h, x:x+w]
        
        cv2.imwrite(path, face)
        count = count + 1
       

total = count
        
print(" Total Image collected",total)
cap.release()