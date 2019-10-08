import cv2
import os
from PIL import Image
import numpy as np
import pickle

face_cascade = cv2.CascadeClassifier('cascades/data/haarcascade_frontalface_default.xml')
# new_user = input("Enter Student Name:")

def detect_face(frame , img_id , user_dir , new_user):
	gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
	face_rects = face_cascade.detectMultiScale(gray , scaleFactor=1.2, minNeighbors=5)

	for (x,y,w,h) in face_rects:
		cv2.rectangle(frame , (x,y) , (x+w,y+h) ,(255,255,255),5)
		font = cv2.FONT_HERSHEY_SIMPLEX
		cv2.putText(frame ,'registering user' + str(new_user) , (x,y) , font , 1 ,(255,0,0) , 2 ,cv2.LINE_AA)
		roi_gray = gray[y:y+h , x:x+w]
		cv2.imwrite(new_user + "\\"+str(img_id)+".jpg", roi_gray)
		if cv2.waitKey(1) & 0xFF == ord('q'):
			break
	return frame

def capture(new_user) :
	os.chdir('images')
	os.mkdir(new_user)
	
	BASE_DIR = os.path.dirname(os.path.abspath(__file__))
	image_dir = os.path.join(BASE_DIR,'images')
	user_dir = os.path.join(image_dir,new_user)
	
	cap = cv2.VideoCapture(0)
	width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
	height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
	img_id = 0
	img_count = 0
	while img_count<=100:
		# if cv2.waitKey(1) & 0xFF == ord('q'):
		# 	break
		img_count=len([name for name in os.listdir(BASE_DIR+"//images//"+str(new_user))])
		print(img_count)
		if img_id % 50 == 0:
			print("Collected ", img_id," images")
		ret, frame = cap.read()
		frame =  detect_face(frame, img_id, user_dir, new_user)
		cv2.imshow('frame',frame)
		img_id+=1

	cap.release()
	cv2.destroyAllWindows()
	return user_dir