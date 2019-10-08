import cv2
import numpy as np
import matplotlib.pyplot as plt
import pickle
# %matplotlib inline
class FacialRecog:
    def __init__(self):
        self.face_cascade = cv2.CascadeClassifier('cascades/data/haarcascade_frontalface_default.xml')
        self.eye_cascade = cv2.CascadeClassifier('cascades/data/haarcascade_eye.xml')
        self.smile_cascade = cv2.CascadeClassifier('cascades/data/haarcascade_smile.xml')

        self.recognizer = cv2.face.LBPHFaceRecognizer_create()
        self.recognizer.read('trainer.yml')

        self.uid = set()

        self.labels = {"person_name":1}
        with open('labels.pickle','rb') as f: #read bytes as file
            og_labels = pickle.load(f) #load file
            self.labels = {v:k for k,v in og_labels.items()}

        # def generate_dataset(img,user_id,img_id):
        #     cv2.imwrite("images/user-" + str(user_id) + "-" + str(img_id) +".jgp",img)

    
    # 0 parameter connects to your computer's default camera
        cap = cv2.VideoCapture(0)


        # Automatically grab width and height from video feed
        # (returns float which we need to convert to integer for later on)
        width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))


        # writer = cv2.VideoWriter('sumedh_capture.mp4', cv2.VideoWriter_fourcc(*'DIVX'),25, (width, height))
        img_id = 0

        #count = 0
        import time
        seconds = time.time() + 20
        
        while True:

            """My Changes"""
            seconds1 = time.time()
            if seconds1>seconds:
                break
            #count+=1
            #print(count)
            """My Changes"""
            
            # Capture frame-by-frame
            self.ret, self.frame = cap.read()

            # Our operations on the frame come here
            # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            self.frame =  self.detect_face(self.frame)

            # Write the video
            # writer.write(frame)

            # Display the resulting frame
            cv2.imshow('frame',self.frame)
            
            img_id+=1

            # This command let's us quit with the q button on a keyboard.
            # Simply pressing X on the window won't work
            
            # EXPLANATION FOR THIS LINE OF CODE:
            # https://stackoverflow.com/questions/35372700/whats-0xff-for-in-cv2-waitkey1/39201163
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        # When everything done, release the capture and destroy the windows
        cap.release()
        # writer.release()
        cv2.destroyAllWindows


        # C:\Users\Sumedh\AppData\Local\Programs\Python\Python36-32\Lib\site-packages\cv2

    def detect_face(self,img):
        face_img = img.copy()
        
        gray = cv2.cvtColor(self.frame,cv2.COLOR_BGR2GRAY)

        face_rects = self.face_cascade.detectMultiScale(gray , scaleFactor=1.2, minNeighbors=5) 
        #returns object which will help in drawing rectangle ie. x,y,w,h 
        

        for (x,y,w,h) in face_rects:
            # print(x,y,w,h)
            roi_gray = gray[y:y+h , x:x+w]
            # cv2.imwrite("images/user-" + str(user_id) + "-" + str(img_id) +".jgp",img)
            # generate_dataset(roi_gray,user_id,img_id)

            
            # OR

            #Recognition : Deep learned model to predict which uses keras/tensorflow/pytorch/scikit-learn etc
            #..which is very difficult. so tried to create my own trainer

            _id , confidence = self.recognizer.predict(roi_gray)

            if confidence>=65: #and confidence<=85:
                """My Changes"""
                try:
                    self.uid.add(int(self.labels[_id]))
                except:
                    pass
                """My Changes"""

                #print("\n" + str(_id) + "\n")
                #print("\n" + str(self.labels[_id]) + "\n")
                # font = cv2.FONT_HERSHEY_SIMPLEX
                # name = labels[_id]
                # color = (255,255,255)
                # stroke = 2
                # cv2.PutText(frame, name, (x,y),font,1,stackoverflowtroke,cv2.LINE_AA)
                font = cv2.FONT_HERSHEY_SIMPLEX
                cv2.putText(face_img,self.labels[_id] ,(x,y) , font ,1,(255,0,0) ,2,cv2.LINE_AA)
                # cv2.putText(frame, text=labels[_id] , org=(x,y) , fontFace=font , fontScale= 20 , color=(255,0,0) , thickness=10,lineType=cv2.LINE_AA)

            cv2.rectangle(face_img, (x,y), (x+w,y+h), (255,255,255), 5)
            #PARAMETERS: img_variable, pt1 ie top-left, pt2 ie bottom-right, colour,thickness of lines

        return face_img