#!/usr/bin/python3

# import necessary module
import numpy as np
import cv2



# function to identify the face
# arguments -> dictionary of student_id as key and student_name as value

def identify(info_dic):
	# create classifier object using haar cascade
	face_cascade = cv2.CascadeClassifier('recognizer_module/data/haarcascade_frontalface_default.xml')

	# create object of LBPH face recognizer
	rec=cv2.face.LBPHFaceRecognizer_create()
	# rec.read('trainingdata.yml')


	# load the yml file (trained_model)

	rec.read('recognizer_module/recognizer/trainingdata.yml')
	
	# specify font style
	fontface= cv2.FONT_HERSHEY_SIMPLEX
	# specify font scale
	fontscale=1
	# specify font color
	fontColor=(0,255,0)


	# create webcam object
	cam=cv2.VideoCapture(0)


	i=0
	while i<500:


		# read frame from the webcam object

		_,frame = cam.read()

		# convert into grayscale 
		gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

		# detect face using face_cascade object
		faces = face_cascade.detectMultiScale(gray,1.3,5)


		for (x,y,w,h) in faces:

			# create rectangle on detected face
			cv2.rectangle(frame , (x,y) , (x+w , y+h) ,(255,0,0),2)

			# predict the id and confidence level of the detected face
			id_ , confd = rec.predict(gray[y:y+h , x:x+w])

			
			# if confidance level is greated than 60 than the rectangle show on the detected face

			if confd>=60 :
				
				# put the name on the detected as per the actual name saved in database
				name = info_dic[id_]
				cv2.putText(frame,name,(x,y+h),fontface,fontscale,fontColor)
				cv2.putText(frame,str(confd),(x+w,y+h),fontface,fontscale,fontColor)

		# show the detected image
		cv2.imshow('image',frame)
		i+=1
		if cv2.waitKey(1) & 0xff == ord('q'):
			break
		

	# release webcam object 	

	cam.release()	
	# destroy all windows		
	cv2.destroyAllWindows()	

	# return id and confidence level
	return id_,confd

