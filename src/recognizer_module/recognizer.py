#!/usr/bin/python3

import numpy as np
import cv2





def identify(info_dic):
	face_cascade = cv2.CascadeClassifier('recognizer_module/data/haarcascade_frontalface_default.xml')
	rec=cv2.face.LBPHFaceRecognizer_create()
	# rec.read('trainingdata.yml')

	rec.read('recognizer_module/recognizer/trainingdata.yml')
	
	fontface= cv2.FONT_HERSHEY_SIMPLEX
	fontscale=1
	fontColor=(0,255,0)

	cam=cv2.VideoCapture(0)

	# for i in range(5000):
	i=0
	while i<5000:

		_,frame = cam.read()
		gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

		faces = face_cascade.detectMultiScale(gray,1.3,5)

		for (x,y,w,h) in faces:

			cv2.rectangle(frame , (x,y) , (x+w , y+h) ,(255,0,0),2)
			id_ , confd = rec.predict(gray[y:y+h , x:x+w])

			print(id_)
			print('*****************')
			print(info_dic)

			if confd>=60 and confd <= 85:
			# print(ids)
			# print(conf)
				name = info_dic[id_]
				cv2.putText(frame,name,(x,y+h),fontface,fontscale,fontColor)
				cv2.putText(frame,str(confd),(x+w,y+h),fontface,fontscale,fontColor)

		cv2.imshow('image',frame)
		i+=1
		if cv2.waitKey(1) & 0xff == ord('q'):
			break
		# if i >50:
		# 	break

		

	cam.release()			
	cv2.destroyAllWindows()	

	return id_,confd

