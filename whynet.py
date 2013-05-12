#!/usr/bin/python2
import sys, urllib2, os, re, argparse

# get arguments
parser = argparse.ArgumentParser(description='Download video from Ynet (and Hot & Reshet).')
parser.add_argument('url', help = 'page url')
parser.add_argument('-o', dest = 'file', help = 'output file')
args = parser.parse_args()
	
url = args.url
page = urllib2.urlopen(url).read()

link = (re.search('(rtmp%3A%2F%2F((?!%22).)*)%22',page))
if link is None: 
	print "Clip not found!"
	exit()
link = urllib2.unquote(link.group(1)) 

if args.file is None:
	filename = os.path.basename(link)
else:
	filename = args.file
print ("Download: " + link)
os.system('rtmpdump -r ' + link + " -o " + filename)
