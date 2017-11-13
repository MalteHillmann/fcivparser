# fcivparser
Converts the output of the Microsoft File Checksum Integrity Verifier (FCIV) to md5sum/sha1sum compatible format

# Features
* Converts MD5- and/or SHA1-sums from XML-File created by FCIV to "standard" hex formatted Hashsums.
* When converting only MD5 or only SHA1 it creates a md5sum or sha1sum compatible format
* You can check your hashes against the files with md5sum/sha1sum
* You can strip slashes, because md5sum and sha1sum wont work with pathes that contains backslashes. (only useful, if you have only one level of files to check)

# Usage
```usage: fcivparser.py [-h] [-s] infile [infile ...]

Process the XML output of Microsoft File Checksum Integrity Verifier
(FCIV.exe).

positional arguments:
  infile           XML file(s) that will be processed

optional arguments:
  -h, --help       show this help message and exit
  -s, --strippath  Strips the path from all files
```

# Author

* Sourcecode is based on the Script [hashparser.py](https://github.com/xme/powershell_scripts/blob/master/hashparser.py)
* Enhanced by Malte F. Hillmann
