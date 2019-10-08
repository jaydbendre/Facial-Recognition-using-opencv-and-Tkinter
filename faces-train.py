import cv2
import os
from PIL import Image
import numpy as np
import pickle

BASE_DIR = os.path.dirname(os.path.abspath(__file__)) 
# gets path of where file is saved in system
image_dir = os.path.join(BASE_DIR,'images')
# takes in base directory and looks for images folder

face_cascade = cv2.CascadeClassifier('cascades/data/haarcascade_frontalface_default.xml')

current_id = 0
label_ids = {}
	
y_labels = []
x_train = []


for root, dirs, files in os.walk(image_dir):
	
	for file in files:

		if file.endswith('png') or file.endswith('jpg') or file.endswith('JPG'):
			
			# gets path of images stored in images folder
			path = os.path.join(root,file)
	 		
			# gets label for images from directories
			# ie giving images of a particular person a label since their filename is saves as 1,2,3..
			label = os.path.basename(os.path.dirname(path)).replace(" ","-").lower()
			# replace every " " with "-" in case you have any and lower case them
			
			#print(label,path)

			#to create training labels ie ID for roi

			# if label in label_ids:
			# 	pass
			# else:
			# 	label_ids[label] = current_id
			# 	current_id += 1
			
			if not label in label_ids:
				label_ids[label] = current_id
				current_id += 1
			# if label is not present then we actually create a dictionary with the label(person's name) and an id associated to it

			_id = label_ids[label]
			#print(label_ids)

			# y_labels.append(label) # some number
			# x_train.append(path) # verify this image , turn it into a numpy array , convert to GRAY

			pil_image = Image.open(path).convert('L') # L converts it to grayscale
			#for better recognition
			size=(550,550)
			final_image = pil_image.resize(size,Image.ANTIALIAS)
			image_array = np.array(final_image,'uint8')
			#print(image_array)
			
			face_rects = face_cascade.detectMultiScale(image_array , scaleFactor=1.2, minNeighbors=5)

			# ROI for training data
			for (x,y,w,h) in face_rects:
				roi = image_array[y:y+h , x:x+w]
				x_train.append(roi)
				y_labels.append(_id)
			#to create training labels ie ID for roi

# print(y_labels)
# print(x_train)

# Using Pickle to save label Ids 
# for serializing and de-serializing a Python object structure
# similar to JSON
# https://thepythonguru.com/pickling-objects-in-python/

with open('labels.pickle','wb') as f: #writing bytes as file
	pickle.dump(label_ids , f) #dump label_ids in file

# TRAIN OPENCV RECOGNIZER

recognizer = cv2.face.LBPHFaceRecognizer_create()

recognizer.train(x_train , np.array(y_labels))
recognizer.save('trainer.yml')

# IMPLEMENT RECOGNIZER