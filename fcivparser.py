#!/usr/bin/python
#
# Convert XML with hashes to CSV files
# Thanks to @ddurvaux for sharing!
#
# Contribution: Malte F. Hillmann
#
import xml.etree.ElementTree as etree
import argparse
import base64
import ntpath

# configure arguments accepted by this script
parser = argparse.ArgumentParser(description='Process the XML output of Microsoft File Checksum Integrity Verifier (FCIV.exe).')
parser.add_argument('infile', nargs='+', help='XML file(s) that will be processed')
parser.add_argument('-s','--strippath', action='store_true', help='Strips the path from all files')
args = parser.parse_args()

# Loop on the files provided as argument
for filename in args.infile:
	try:
		root = etree.parse(filename).getroot()
		for n in root.findall("FILE_ENTRY"):
			name = n.find("name").text
			if args.strippath:
				name = ntpath.basename(name)
			MD5 = base64.b64decode(n.find("MD5").text).encode("hex") if n.find("MD5") is not None else None
			SHA1 = base64.b64decode(n.find("SHA1").text).encode("hex") if n.find("SHA1") is not None else None
			if SHA1 == None:
				print "%s  %s" % (MD5, name)
			if MD5 == None:
				print "%s  %s" % (SHA1, name)
			if SHA1 != None and MD5 != None:
				print "%s, %s, %s" % (name, MD5, SHA1)
	except:
		print "FATAL ERROR while parsing %s" % (filename)
