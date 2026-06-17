import cv2
import os
import numpy as np

os.makedirs("dataset/Bhagyashri", exist_ok=True)
images = os.listdir("dataset/Bhagyashri")

faces = []
label =[]

for image in images:
    print(image)

    path = f"dataset/Bhagyashri/{image}"   
    
    img = cv2.imread(path, cv2.IMREAD_GRAYSCALE) 
        
    faces.append(img)
    label.append(0)
        
    # cv2.imshow("Image Showing", img)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

labels = np.array(label)

recognizer = cv2.face.LBPHFaceRecognizer_create()

recognizer.train(faces, labels)

recognizer.save("trainer.yml")

print("Training Completed!")
    
# print(len(faces))
# print(type(faces[0]))
# print(len(label))
# print(type(label[0]))
