#! python3
#Mass archiving of multiple directories
import sys
import os		#Directory Management
import zipfile	#File compression
import argparse	#Argument Handling

def subZip(zf, sourceDir):
	"""Attempt to add all files and directories in a folder to a given zip file.
		Keyword Arguments:
		zf -- Zip file to be written to.
		sourceDir -- String representation of the directory's contents to be added
	"""
	#Get all local files
	allLocalFiles = os.listdir(sourceDir)					
	#Loop through file names
	for f in allLocalFiles:
		#Add a file to archive									
		zf.write(sourceDir + "\\" + f)						
		#If file added is a directory Recursively add subdirectory files
		if os.path.isdir(sourceDir+ "\\" + f):				
			subZip(zf, sourceDir + "\\" + f)				

def zipDirectory(sourceDir, targetDir, compression=False):
	"""Begin archiving a given directroy
		Keyword Arguments:
		sourceDir -- String representation of the directory to be archived
		targetDir -- String representation of the location to save the given directory
	"""
	sourceStr = targetDir + "\\" + os.path.basename(sourceDir) + ".zip"		#String representation of archive location
	print("Archiving "+ sourceDir + " to " + sourceStr)
	zf = zipfile.ZipFile( sourceStr, 'w', zipfile.ZIP_DEFLATED)	if compression else zipfile.ZipFile( sourceStr, 'w')
	if(compression):
		print("Compression is ON for " + sourceStr)
	#Add all sub-files
	subZip(zf, sourceDir)									
	zf.close()	#Close directory file

def buildTo(sourceList, targetDir = None, compression=False, gen = False):
	"""Confirms desired destination directory is available and initiates archiving on sourceList
		Keyword Arguments:
		sourceList -- List of all directories to be operated on
		targetDir -- Destination to save all archive files. If None, save in cwd
		compression -- User request to compress zip archives
	"""
	#If expected target directory is inaccessible or undefined
	if(targetDir is None or not os.path.isdir(targetDir)):	
		print("Target directory " + targetDir + " inaccessible")
		if(gen):
			os.makedirs(targetDir)
			print("Generating target directory: " + targetDir)
		else:
			print("Building in local directory")
			targetDir = ""	#Build locally (equivalent to .)
	#Iterate through list of directories
	for f in sourceList:									
		zipDirectory(f, targetDir, compression)	

def getSourceDirs(targetRoot = None):
	"""Get all directories in a given destination. 
	 	Keyword Arguments:
	 	targetRoot -- String representation of target folder. If none, works "."
 	""" 
	targetDirs = []
	for f in os.listdir(targetRoot):
		folder = f#os.path.abspath(targetRoot) + "\\" + f
		print(os.path.abspath(folder))
		if os.path.isdir(folder):
			targetDirs.append(folder)						
	return targetDirs
	#RETURNS: list of strings, directory names

#############################################################
#															#
#------------------Main Loop--------------------------------#
#															#
#############################################################

def main(argv):												#Run version check and execute script if valid
	if(sys.version_info.major < 3):							#Shebang line not read or Py3 not available on local PC
		sys.stdout.write("Please use Python 3 or above.")	#Inform user of error
		return -1											#RETURNS: -1
	
	parser = argparse.ArgumentParser(description="Create ZIP archives of all directories in a given folder")
	parser.add_argument("dest", help="Destination of generated archives")
	parser.add_argument("--src", "-s", help="Location of folders to be archived (defaults to current working directory).")
	parser.add_argument("-c", "--compress", help="Compress generated archives", action="store_true")
	parser.add_argument("-g", "--generate", help="Generate destination directory if not present.", action = "store_true")
	args = parser.parse_args()

	os.chdir(args.src)

	lst = getSourceDirs()							#Get list of directories
	#Opted for less detsructive version as temporary solution to issue #1
	if args.dest in lst:
		lst.remove(args.dest)
	buildTo(lst, args.dest, args.compress, args.generate)#Archive list to destination
	print("Mass archiving complete.")
	return 0												#RETURNS: 0

if __name__ == "__main__":
	main(sys.argv)