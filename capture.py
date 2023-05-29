# from database import *
from flask import *
# import demjson
import numpy as np
from model_manager import Model
import pickle
import math
import cv2
import uuid

import face_recognition
import argparse

from imutils import paths
import os
import requests
import io
import json
# from database import *
from datetime import datetime



# //////////////////////////////////////////////////////////////////////
# camera for image testing
def captures(pid):
	size = 4


	# We load the xml file
	classifier = cv2.CascadeClassifier('haarcascade_frontalface_alt.xml')

	webcam = cv2.VideoCapture(0) #Using default WebCam connected to the PC.
	(rval, im) = webcam.read()
	flag=0
	i=0
	while True:
		if i<=10:
			(rval, im) = webcam.read()
			im=cv2.flip(im,1,0) #Flip to act as a mirror

			# Resize the image to speed up detection
			mini = cv2.resize(im, (int(im.shape[1]/size), int(im.shape[0]/size)))

			# detect MultiScale / faces 
			faces = classifier.detectMultiScale(mini)

			# Draw rectangles around each face
			flag=0

			for f in faces:
				(x, y, w, h) = [v * size for v in f] #Scale the shapesize backup
				cv2.rectangle(im, (x,y), (x+w,y+h), (0,255,0), 4)

				#Save just the rectangle faces in SubRecFaces
				sub_face = im[y:y+h, x:x+w]
				isFile = os.path.isdir("static/trainimages/"+str(pid))  
				print(isFile)
				if(isFile==False):
					os.mkdir('static\\trainimages\\'+str(pid))
				FaceFileName = "static/trainimages/"+str(pid)+"/"+str(uuid.uuid4())+".jpg" #Saving the current image from the webcam for testing.
				print(FaceFileName)

				cv2.imwrite(FaceFileName, sub_face)
				i=i+1
		else:
			flag=1

			# break
			# val=rec_face_image(FaceFileName)
			
					
					
		cv2.imshow('Capture(Press Esc to exit)',   im)
		key = cv2.waitKey(10)
		print(f"key : {key}")
		# # if Esc key is press then break out of the loop 
		if key == 27: #The Esc key
			return FaceFileName
			break

		if flag==1:
			return FaceFileName
			break
			
	
