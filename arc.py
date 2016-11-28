#! python3
#Mass archiving of multiple directories
import sys
import os		#Directory Management
import zipfile	#File compression

def subZip(zf, sourceDir):									#Attempt to add all subfiles 
	allLocalFiles = os.listdir(sourceDir)					#Get all local files
	for f in allLocalFiles:									#Loop through file names
		zf.write(sourceDir + "\\" + f)						#Add a file to archive
		if os.path.isdir(sourceDir+ "\\" + f):				#If file added is a directory
			subZip(zf, sourceDir + "\\" + f)				#Recursively add subdirectory files

def zipDirectory(sourceDir, targetDir):						#Begin archiving of a single directory
	sourceStr = targetDir + "\\" + sourceDir + ".zip"		#String representation of archive location
	print("Archiving "+ sourceDir + " to " + sourceStr)
	zf = zipfile.ZipFile( sourceStr, 'w')					#Create Zip file
	subZip(zf, sourceDir)									#Add all sub-files
	zf.close()												#Close directory file

def buildTo(sourceList, targetDir = None):
	if(targetDir is None or not os.path.isdir(targetDir)):	#Expected target directory is inaccessible or undefined
		print("Target directory " + targetDir + " inaccessible")
		targetDir = ""										#Build locally
	for f in sourceList:									#Iterate through list of directories
		zipDirectory(f, targetDir)							#Create zip archive of each directory (uncompressed)

def getSourceDirs(targetRoot = None):
	targetDirs = []											#Initialize list
	if(targetRoot != None):									#User specifies files are located elsewhere
		print("Attempting CD to " + targetRoot)				#Currently can do nothing
		#TODO: Finish Attempt CD subroutine
		print("CD failed. Building archives in place.")
	allLocalFiles = os.listdir()							#Get all local files
	for f in allLocalFiles:									#Loop through file names
		if os.path.isdir(f):								#If a file is a directory
			targetDirs.append(f)							#Add directory to return list
	return targetDirs										#RETURNS: list of strings, directory names

def main():													#Run version check and execute script if valid
	if(sys.version_info.major < 3):							#Shebang line not read or Py3 not available on local PC
		sys.stdout.write("Please use Python 3 or above.")	#Inform user of error
		return -1											#RETURNS: -1
	lst = getSourceDirs()
	buildTo(lst, "..\\build")
	print("Mass archiving complete.")
	return 0												#RETURNS: 0

if __name__ == "__main__":
	main()