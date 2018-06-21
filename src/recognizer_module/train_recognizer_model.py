#!/usr/bin/python3


# import necessary modules
import os
import numpy as np
import cv2


# function to train the model
def train():

	# list to store all the detected face-array
	faces=[]
	# student_id of the detected face
	IDs=[]

	# specify the base directory < location of this file>
	RECOG_BASE_DIR = os.path.dirname(os.path.abspath(__file__))

	# specify the image directory (base_dir/images)
	image_dir = os.path.join(RECOG_BASE_DIR, "images")


	# create LBPH face rcognizer object
	recognizer=cv2.face.LBPHFaceRecognizer_create()
	
	# loop to get all  absolute path of images file in image directory
	for root, dirs, files in os.walk(image_dir):
		for file in files:
			if file.endswith("png") or file.endswith("jpg"):
				# absolute path
				path = os.path.join(root, file)
				
				# read image
				image = cv2.imread(path,0)
				# convert into numpy array of dtype=uint8
				face_array = np.array(image, "uint8")

				# append image array in faces
				faces.append(face_array)
				# append student_id of the corresponding face  in IDs
				IDs.append(int(path.split('/')[-2].split('-')[1]))


	# train the recognizer model
	# serving face and IDs of numpy array type
	recognizer.train(faces,np.array(IDs))
	# save the trained model for future prediction
	recognizer.write('recognizer_module/recognizer/trainingdata.yml')

	return        	