Mass Archive Tool
Version 1.0
(c) Mark Fitzgibbon 2016

+-----------+
|Description|
+-----------+
Python based tool for archiving of multiple directories.

+--------+
|Download|
+--------+
User can pull, fork, or download tool from 
https://github.com/ibbolia/Mass-Archive

+------------+
|Requirements|
+------------+
Mass Archive currently requires Python 3.x installed (Tested with Py3.5)
Compression feature requires zlib module to be installed

+-----+
|Usage|
+-----+
usage: MassArchive.py [-h] [--src SRC] [-c] dest

Create ZIP archives of all directories in a given folder

positional arguments:
  dest               Destination of generated archives

optional arguments:
  -h, --help         show this help message and exit
  --src SRC, -s SRC  Location of folders to be archived (defaults to current
                     working directory).
  -c, --compress     Compress generated archives

+-------+
|Contact|
+-------+
Github: https://github.com/ibbolia
Twitter: @ibbolia
Gmail: mwfitzgibbon