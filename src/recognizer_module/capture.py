#!/usr/bin/python3


# import necessary module
import numpy
import cv2
import os





# define function to capture data to train model
# arguments ( student_name , student_id )

def Capture(labal,id_):
	# counter to take no. of sample photos
	sampleNo = 0

	# create classifier object using Haar cascade
	face_cascade = cv2.CascadeClassifier('recognizer_module/data/haarcascade_frontalface_default.xml')

	# create camera object
	cam=cv2.VideoCapture(0)

	# create directory named as -> student_name-student_id
	dir_name = 'recognizer_module/images/'+labal+'-'+str(id_)
	os.mkdir(dir_name)


	while True:

		# read frame from webcam
		_,frame = cam.read()

		# convert into gray
		gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
		# convert into gauss for more accuracy
		gauss = cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,115,1)

		# detect face form the frame using classifier object
		faces = face_cascade.detectMultiScale(gauss, 1.3, 5)


		for (x,y,w,h) in faces:

			sampleNo+=1
			# take detected portion and resize into 100,100
			roi =cv2.resize(gray[y:y+h,x:x+w],(100,100))
			# save face image as sample_no.jpg
			file_name = "{}/{}.jpg".format(dir_name,sampleNo)
			cv2.imwrite(file_name,roi)

			# draw rectangle on detected face of the frame
			cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)

		# show the frame with detected part 
		cv2.imshow('image',frame)
		cv2.waitKey(1)	
		# take 50 samples only  
		if sampleNo>50:
			break

	# release cam object and destroy all windows created
	cam.release()			
	cv2.destroyAllWindows()

	return
	
