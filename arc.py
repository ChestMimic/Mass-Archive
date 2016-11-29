#! python3
#Mass archiving of multiple directories
import sys
import os		#Directory Management
import zipfile	#File compression
#import getopt	#Argument handling
import argparse	#Argument Handling

#def usage():
#	print("python arc.py src=sourcePath dst=destinationPath")

def subZip(zf, sourceDir):
	'''Attempt to add all files and directories in a folder to a given zip file.
	Keyword Arguments:
	zf -- Zip file to be written to.
	sourceDir -- String representation of the directory's contents to be added
	'''
	allLocalFiles = os.listdir(sourceDir)					#Get all local files
	for f in allLocalFiles:									#Loop through file names
		zf.write(sourceDir + "\\" + f)						#Add a file to archive
		if os.path.isdir(sourceDir+ "\\" + f):				#If file added is a directory
			subZip(zf, sourceDir + "\\" + f)				#Recursively add subdirectory files

def zipDirectory(sourceDir, targetDir):
	'''Begin archiving a given directroy
	Keyword Arguments:
	sourceDir -- String representation of the directory to be archived
	targetDir -- String representation of the location to save the given directory
	'''
	sourceStr = targetDir + "\\" + sourceDir + ".zip"		#String representation of archive location
	print("Archiving "+ sourceDir + " to " + sourceStr)
	zf = zipfile.ZipFile( sourceStr, 'w')					#Create Zip file
	subZip(zf, sourceDir)									#Add all sub-files
	zf.close()												#Close directory file

def buildTo(sourceList, targetDir = None):
	'''Confirms desired destination directory is available and initiates archiving on sourceList
	Keyword Arguments:
	sourceList -- List of all directories to be operated on
	targetDir -- Destination to save all archive files. If None, save in cwd
	'''
	if(targetDir is None or not os.path.isdir(targetDir)):	#Expected target directory is inaccessible or undefined
		print("Target directory " + targetDir + " inaccessible")
		targetDir = ""										#Build locally
	for f in sourceList:									#Iterate through list of directories
		zipDirectory(f, targetDir)							#Create zip archive of each directory (uncompressed)

def getSourceDirs(targetRoot = None):
	'''Get all directories in a given destination. 
	Keyword Arguments:
	targetRoot -- String representation of target folder. If none, works on cwd
	''' 
	targetDirs = []											#Initialize list
	if(targetRoot != None):									#User specifies files are located elsewhere
		print("Attempting CD to " + targetRoot)				#Currently can do nothing
		os.chdir(targetRoot)
	allLocalFiles = os.listdir()							#Get all local files
	for f in allLocalFiles:									#Loop through file names
		if os.path.isdir(f):								#If a file is a directory
			targetDirs.append(f)							#Add directory to return list
	return targetDirs										#RETURNS: list of strings, directory names

def main(argv):												#Run version check and execute script if valid
	if(sys.version_info.major < 3):							#Shebang line not read or Py3 not available on local PC
		sys.stdout.write("Please use Python 3 or above.")	#Inform user of error
		usage()
		return -1											#RETURNS: -1
	
	#dstDir = None
	#srcDir = None

	parser = argparse.ArgumentParser(description="Create ZIP archives of all directories in a given folder")
	parser.add_argument("dest", help="Destination of generated archives")
	parser.add_argument("--src", "-s", help="Location of folders to be archived (defaults to current working directory).")
	#parser.add_argument("-c", "--compress", help="Compress generated archives[NOT IMPLEMENTED]", action="store_true")
	args = parser.parse_args()

	lst = getSourceDirs(args.src)							#Get list of directories
	buildTo(lst, args.dest)									#Archive list to destination
	print("Mass archiving complete.")
	return 0												#RETURNS: 0

if __name__ == "__main__":
	main(sys.argv)