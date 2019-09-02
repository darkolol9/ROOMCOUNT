import numpy as np
from PIL import ImageGrab
import cv2
from matplotlib import pyplot as plt
from math import sqrt 
import pytesseract
import os
import time
import tkinter as tk
import OCR

zero = [cv2.imread("resources/bitmaps/0.bmp"),'0',0]
nine = [cv2.imread("resources/bitmaps/9.bmp"),'9',0]
seven = [cv2.imread("resources/bitmaps/7.bmp"),'7',0]
plus = [cv2.imread("resources/bitmaps/+.bmp"),'+',0]
six = [cv2.imread("resources/bitmaps/6.bmp"),'6',0]
two = [cv2.imread("resources/bitmaps/2.bmp"),'2',0]
eight = [cv2.imread("resources/bitmaps/8.bmp"),'8',0]
three = [cv2.imread("resources/bitmaps/3.bmp"),'3',0]
four = [cv2.imread("resources/bitmaps/4.bmp"),'4',0]
minus = [cv2.imread("resources/bitmaps/-.bmp"),'-',0]
precent = [cv2.imread("resources/bitmaps/%.bmp"),'%',0]
one = [cv2.imread("resources/bitmaps/1.bmp"),'1',0]
colon = [cv2.imread("resources/bitmaps/colon.bmp"),':',0]
five = [cv2.imread("resources/bitmaps/5.bmp"),'5',0]

bitmaps = [zero,one,colon,five,minus,precent,two,three,four,six,seven,eight,nine,plus]


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
	inverted_time = cv2.bitwise_not(formatted_time)

	time_str = OCR.apply_ocr(bitmaps,inverted_time)
	print(time_str)

	frame = cv2.cvtColor(formatted_scrnsht, cv2.COLOR_BGR2RGB)
	invertedmap = cv2.cvtColor(room, cv2.COLOR_BGR2RGB)

	threshold = 0.7711001000000
	res = cv2.matchTemplate(frame, room, cv2.TM_CCOEFF_NORMED)
	loc = np.where(res >= threshold)
	#print(loc
	w, h,__ = room.shape

	for pt in zip(*loc[::-1]):

		cv2.rectangle(frame, pt, (pt[0] + w, pt[1] + h), (0,0,255) ,1)

		count = count + 1

	print('number of rooms is: ' ,int(count/10+1))
	time.sleep(4)
	os.system('cls')
	



    










#to do - check for intersection between images