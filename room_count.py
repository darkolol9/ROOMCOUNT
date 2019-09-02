import cv2
import numpy as np
from PIL import ImageGrab
import time as TIME
import os


#img = cv2.imread('resources/test_imgs/map3.png') #example map

img2 = cv2.imread('resources/mask.png') #mask tool
template = cv2.imread('resources/masked_2.png') #masked single room

print('loaded resources successfully! begining to count rooms..\n')


#now to look for a single masked room in the combined screenshot + mask
while 1:
	TIME.sleep(4)
	os.system('cls')

	count = 0

	scrnshot = ImageGrab.grab(bbox = (99,23,381,305)) #first screenshot of map
	formatted_scrnsht = np.array(scrnshot)
	img = cv2.cvtColor(formatted_scrnsht, cv2.COLOR_BGR2RGB)  

	dst = cv2.addWeighted(img,0.7,img2,0.7,0)  #mask the screenshot
	threshold = 0.997 #accuracy threshold 997 was working fine

	res = cv2.matchTemplate(dst,template,cv2.TM_CCORR_NORMED) #find the matches
	loc = np.where(res >= threshold)

	for pt in zip(*loc[::-1]): #count
		count = count + 1

	print('\t number of rooms:',count)    

	




input()


