#a simple program to ove files from one directory to the other


import os
import shutil #the module that helps to move the files

pics=('/home/netshadow/Music') #the destination directory
for (path, dirs, files) in os.walk( '/home/netshadow/Pictures'):
#	print (dirs)
#	print (files)
	for filename in files:
		if filename == (filename,'*.jpeg') or filename[-4:]== '.jpeg' or filename[-4:] == '.pdf' or filename[-4:] == '.mp4' or filename == (filename, "*.mp3"):
			paths=os.path.join(path,filename)
			shutil.move(paths,pics)
			print ("done")
			
