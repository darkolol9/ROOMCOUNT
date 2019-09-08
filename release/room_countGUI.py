import cv2
import numpy as np
from PIL import ImageGrab
import os


import tkinter as tk

img2 = cv2.imread('resources/mask.png') #mask tool
template = cv2.imread('resources/masked_2.png') #masked single room

print('loaded resources successfully! begining to count rooms..\n')

def hide_bar(root,b):
	xloc = root.winfo_x()
	yloc = root.winfo_y()
	xlocstr = str(xloc+6)
	ylocstr = str(yloc+27)
	root.overrideredirect(1)
	root.geometry('+'+xlocstr+'+'+ylocstr)
	b.pack_forget()

def countrooms(seconds,root):
	os.system('cls')

	count =0
	xloc = root.winfo_x()
	yloc = root.winfo_y()

	scrnshot = ImageGrab.grab(bbox = (xloc,yloc,xloc+282,yloc+282)) #first screenshot of map
	
	print('updated:   + ' ,xloc,' ',yloc, ' \n')

	formatted_scrnsht = np.array(scrnshot)

	img = cv2.cvtColor(formatted_scrnsht, cv2.COLOR_BGR2RGB)  

	dst = cv2.addWeighted(img,0.7,img2,0.7,0)  #mask the screenshot
	threshold = 0.997 #accuracy threshold 997 was working fine

	res = cv2.matchTemplate(dst,template,cv2.TM_CCORR_NORMED) #find the matches
	loc = np.where(res >= threshold)

	for pt in zip(*loc[::-1]): #count
		count = count + 1

	if count == 0:
		seconds = 0 
	else:
		seconds = seconds + 2	

	rpm =0

	if seconds !=0:
		rpm = (count/ (seconds/60))

	rpm_string = "{:.2f}".format(rpm)
	estimated_time = 'N/A'

	if rpm != 0:
		estimated_time = "{:.2f}".format(57/rpm)
	else:
		estimated_time = 'N/A'	

	seconds_str = str(seconds)	

	roomsleft1 = str(64 - count)
	roomsleft2 = str(50-count)	

	string = 'Rooms open: ' + str(count) + ' RPM: '  +  rpm_string + " (estimated end time: " + estimated_time + ")" 
	#print(string)

	w.config(text = string)
	root.after(2000,countrooms,seconds,root)




root = tk.Tk()
root.geometry("281x281")
root.overrideredirect(0)
root.configure(background='black')
w = tk.Label(root, text='0',background ='black',fg='white',font='helvetica 8')
b = tk.Button(root,text='hide bar',command = lambda: hide_bar(root,b))
b.pack()
w.pack()

seconds = 0

countrooms(seconds,root)
root.attributes('-alpha', 0.3)
root.call('wm', 'attributes', '.', '-topmost', '1')  


root.mainloop()
