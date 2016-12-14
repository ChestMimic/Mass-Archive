Mass Archive Tool
=================
Version 0.2
-----------
(c) Mark Fitzgibbon 2016

Description
-----------
Python based tool for archiving of multiple directories.

Download
--------
User can pull, fork, or download tool from the [Mass-Archive Repository](https://github.com/ibbolia/Mass-Archive)


Requirements
------------
Mass Archive currently requires Python 3.x installed (Tested with Py3.5)
Compression feature requires zlib module to be installed


Usage
-----
    MassArchive.py [-h] [--src SRC] [-c] [-g] dest

Create ZIP archives of all directories in a given folder

Positional arguments:

Argument|Description
-------|-------
dest|Destination of generated archives

Optional arguments:

Argument|Description
-------|-------
-h, --help|Show help message and exit
--src SRC, -s SRC|Location of folders to be archived (defaults to current working directory).
-c, --compress|Compress generated archives
-g, --generate|Generate destination directory if not present

Contact
-------
[Github](https://github.com/ibbolia)

Twitter: [@ibbolia](https://twitter.com/[username])

Gmail: mwfitzgibbon