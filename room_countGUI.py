import cv2
import numpy as np
from PIL import ImageGrab
import os


import tkinter as tk

img2 = cv2.imread('resources/mask.png') #mask tool
template = cv2.imread('resources/masked_2.png') #masked single room

print('loaded resources successfully! begining to count rooms..\n')

def countrooms():
	os.system('cls')

	count =0

	scrnshot = ImageGrab.grab(bbox = (99,23,381,305)) #first screenshot of map
	time_shot = ImageGrab.grab(bbox= (22,28,80,43))

	print('updated\n')

	formatted_scrnsht = np.array(scrnshot)

	img = cv2.cvtColor(formatted_scrnsht, cv2.COLOR_BGR2RGB)  
	
	dst = cv2.addWeighted(img,0.7,img2,0.7,0)  #mask the screenshot
	threshold = 0.997 #accuracy threshold 997 was working fine

	res = cv2.matchTemplate(dst,template,cv2.TM_CCORR_NORMED) #find the matches
	loc = np.where(res >= threshold)

	for pt in zip(*loc[::-1]): #count
		count = count + 1

	roomsleft1 = str(64 - count)
	roomsleft2 = str(50-count)	

	string = 'Rooms open:  ' + str(count)	+ ' || at least '+ roomsleft2+' rooms left '  
	#print(string)

	w.config(text = string)
	root.after(2000,countrooms)




root = tk.Tk()
root.geometry("400x22")
root.overrideredirect(1)
w = tk.Label(root, text='0')
w.pack()
seconds = 0

countrooms()

root.call('wm', 'attributes', '.', '-topmost', '1')  


root.mainloop()
