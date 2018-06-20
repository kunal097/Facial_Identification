#!/usr/bin/python3


import numpy as np
import cv2

import pickle

face_cascade = cv2.CascadeClassifier('attendance/recog_module/data/haarcascade_frontalface_default.xml')


rec=cv2.face.LBPHFaceRecognizer_create()

rec.read('attendance/recog_module/recognizer/trainingdata.yml')

# ids=0


labels = {}
with open("attendance/recog_module/pickle/face-labels.pickle", 'rb') as f:
	og_labels = pickle.load(f)
	labels = {v:k for k,v in og_labels.items()}









fontface= cv2.FONT_HERSHEY_SIMPLEX
fontscale=1
fontColor=(0,255,0)
cam=cv2.VideoCapture(0)
i=0
while i<50000:
	
	status,frame=cam.read()
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

	faces = face_cascade.detectMultiScale(gray, 1.3, 5)
	for (x,y,w,h) in faces:

		cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
		ids,conf=rec.predict(gray[y:y+h,x:x+w])

		if conf>=60 and conf <= 85:
			print(ids)
			print(conf)
			name = labels[ids]
			cv2.putText(frame,name,(x,y+h),fontface,fontscale,fontColor)


	cv2.imshow('image',frame)
	if cv2.waitKey(1)== ord('q'):
		break
	i+=1	

cam.release()			
cv2.destroyAllWindows()




























"""#!/usr/bin/python3


import numpy as np
import cv2

import pickle
import sys

stu = sys.argv[1]

face_cascade = cv2.CascadeClassifier('attendance/recog_module/data/haarcascade_frontalface_default.xml')


rec=cv2.face.LBPHFaceRecognizer_create()

rec.read('attendance/recog_module/recognizer/trainingdata.yml')

ids=0


labels = {}
with open("attendance/recog_module/pickle/face-labels.pickle", 'rb') as f:
	og_labels = pickle.load(f)
	labels = {v:k for k,v in og_labels.items()}









fontface= cv2.FONT_HERSHEY_SIMPLEX
fontscale=1
fontColor=(0,255,0)
cam=cv2.VideoCapture(0)
# i=0

# def det():
while  True:
	
	status,frame=cam.read()
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

	faces = face_cascade.detectMultiScale(gray, 1.3, 5)
	for (x,y,w,h) in faces:

		cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
		ids,conf=rec.predict(gray[y:y+h,x:x+w])

		if conf>=60 and conf <= 85:
			cv2.putText(frame,name,(x,y+h),fontface,fontscale,fontColor)
			# stu.
			break
			# return ids,conf
			# name = labels[ids]
			

	# i++


		# if conf>=60 and conf <= 85:
		# 	break



	cv2.imshow('image',frame)
	if cv2.waitKey(1)== ord('q'):
		break

cam.release()			
cv2.destroyAllWindows()
	# return ids,conf"""