import os,sys

fileNames = sys.argv[1:]

for fileName in fileNames:
	newfileName = "x"+fileName.replace(".WAV","").lower()
	os.rename(fileName, newfileName)