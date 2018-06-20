#!/usr/bin/python3


# import necessary module
import numpy
import cv2
import os





# define function to capture data to train model
# 

def Capture(labal,id_):

	sampleNo = 0

	face_cascade = cv2.CascadeClassifier('recognizer_module/data/haarcascade_frontalface_default.xml')

	cam=cv2.VideoCapture(0)

	dir_name = 'recognizer_module/images/'+labal+'-'+str(id_)
	os.mkdir(dir_name)


	while True:

		_,frame = cam.read()

		gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

		gauss = cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,115,1)

		faces = face_cascade.detectMultiScale(gauss, 1.3, 5)

		for (x,y,w,h) in faces:

			sampleNo+=1
			roi =cv2.resize(gray[y:y+h,x:x+w],(100,100))

			file_name = "{}/{}.jpg".format(dir_name,sampleNo)
			cv2.imwrite(file_name,roi)
			cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
		cv2.imshow('image',frame)
		cv2.waitKey(1)	

		if sampleNo>50:
			break

	cam.release()			
	cv2.destroyAllWindows()

	return
	
