#Change Log
All notable changes will be tracked in this file

##[Unreleased]
###Changed
- Ability to ignore hidden files (begins with '.')

##[0.2.1] - 2016-12-14
###Changed
- Now changes directory within program (original behavior)
- Zip archives filter out common root, still has top level folder (Fixed #5)
- Will ignore any directory that is in both source and destination locations (Again, fixed #1)

###Known issues 
- Bad handling when trying to archive a zip file into another zip file

##[0.2] - 2016-12-09
###Added
- "generate"/"g" flag functionality (Fixed #4)

###Changed
- Comment structure makes code less disorganized looking

##[0.1] - 2016-12-07
###Added
- This changelog 

###Changed
- Converted Readme to markdown file

###Removed
- Redundant occurence of zipDirectoryC function (combined functionality into zipDirectory)

###Fixed
- Tool can properly handle relative path names as parameters (Fixed #2)
- Tool ignores using target directory as a source directory (Fixed #1)