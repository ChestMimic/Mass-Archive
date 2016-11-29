#! python3
#Mass archiving of multiple directories
import sys
import os		#Directory Management
import zipfile	#File compression
#import getopt	#Argument handling
import argparse	#Argument Handling

def usage():
	print("python arc.py src=sourcePath dst=destinationPath")

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
	
	dstDir = None
	srcDir = None

	parser = argparse.ArgumentParser()
	parser.add_argument("dest", help="Destination of generated archives")
	parser.add_argument("-c", "--compress", help="Compress generated archives[NOT IMPLEMENTED]", action="store_true")
	parser.parse_args()
	'''
	try:
		opts, args = getopt.getopt(argv, "hs:d:", ["help","src=" "dst="])
	except getopt.GetoptError:
		usage()
		sys.exit(2)
	for opt, arg in opts:
		if opt in ("-h", "--help"):
			usage()
			sys.exit()
		elif opt in ("-d", "--dst"):
			dstDir = arg
		elif opt in ("-s", "--src"):
			srcDir = arg
'''
	#lst = getSourceDirs(srcDir)
	#buildTo(lst, dstDir)
	#print("Mass archiving complete.")
	return 0												#RETURNS: 0

if __name__ == "__main__":
	main(sys.argv)