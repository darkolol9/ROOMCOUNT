import numpy as np
from PIL import ImageGrab
import cv2
from matplotlib import pyplot as plt
from math import sqrt 
import pytesseract
import os
import time
import tkinter as tk


timer = 0

room = cv2.imread('resources/4room.png')

while(1):
	i =1
	count = 0
	room = cv2.imread('resources/4room.png')

	scrnshot = ImageGrab.grab(bbox = (99,23,378,302))
	time_shot = ImageGrab.grab(bbox = (19,26,79,44))
	formatted_scrnsht = np.array(scrnshot)
	formatted_time = np.array(time_shot)

	time_str = pytesseract.image_to_string(formatted_time)
	#print(time_str)

	frame = cv2.cvtColor(formatted_scrnsht, cv2.COLOR_BGR2RGB)
	invertedmap = cv2.cvtColor(room, cv2.COLOR_BGR2RGB)




	threshold = 0.7711001000000
	res = cv2.matchTemplate(frame, room, cv2.TM_CCOEFF_NORMED)
	loc = np.where(res >= threshold)
	#print(loc)


	w, h,__ = room.shape
	


	

	for pt in zip(*loc[::-1]):

		cv2.rectangle(frame, pt, (pt[0] + w, pt[1] + h), (0,0,255) ,1)

		count = count + 1

	print('number of rooms is: ' ,int(count/10+1))
	time.sleep(4)
	os.system('cls')
	



    










#to do - check for intersection between images