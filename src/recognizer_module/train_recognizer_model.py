#!/usr/bin/python3

import os
import numpy as np
import cv2


def train():

	faces=[]
	IDs=[]

	RECOG_BASE_DIR = os.path.dirname(os.path.abspath(__file__))
	image_dir = os.path.join(RECOG_BASE_DIR, "images")


	recognizer=cv2.face.LBPHFaceRecognizer_create()
	# print(os.path.dirname(os.path.abspath('manage.py')))

	for root, dirs, files in os.walk(image_dir):
		for file in files:
			if file.endswith("png") or file.endswith("jpg"):
				path = os.path.join(root, file)
				# print(path.split('/')[-2].split('-')[1])

				image = cv2.imread(path,0)
				face_array = np.array(image, "uint8")


				faces.append(face_array)
				IDs.append(int(path.split('/')[-2].split('-')[1]))


	recognizer.train(faces,np.array(IDs))
	# recognizer.save('recognizer_module/recognizer/trainingdata.yml')
	recognizer.write('recognizer_module/recognizer/trainingdata.yml')

	return        	