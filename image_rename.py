from PIL import Image
import os, string

x=0
for f in os.listdir('.'):	
	if f.endswith('.jpg') | f.endswith('jpeg'):
		str= string.ascii_lowercase[x]
		os.rename(f,'Bday 6.06.19_{}.jpg'.format(str))
		x= x+1


