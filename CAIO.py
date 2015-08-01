#!/usr/bin/python

import os
import shutil

#-----------------------------------------------------------

dir_from = "/home/marius/Desktop/from"		#sourch-direction
dir_to = "/home/marius/Desktop/to"			#taget-direction

#-----------------------------------------------------------

count_scanned = 0

	
def copy(file_dir_part, file_name):

	try:
		if os.path.exists(dir_to + "/" + file_name) == False:
			final_dir_from =  dir_from + "/" + file_dir_part + "/" + file_name
			shutil.copy2(final_dir_from, dir_to)	
			print "copied file " + file_name + " in" + dir_to

		else:
			print "File already exists: " + file_name
	
	except:
		print "Can't copy: " + file_name + " !!!"


for f01 in os.listdir(dir_from):
	try:
		for f02 in os.listdir(dir_from + "/" + f01):
			count_scanned += 1
			copy(f01, f02)
	except:
		pass		

#-------------------------------------------------------------

print "\nScanned Files: " 
print count_scanned

print "\nAll done !!!"

