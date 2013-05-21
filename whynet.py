#!/usr/bin/python2
import sys, urllib2, os, re, argparse

# get arguments
parser = argparse.ArgumentParser(description='Download video from Ynet (and Hot).')
parser.add_argument('url', help = 'page url (example: http://www.ynet.co.il/articles/0,7340,L-4302311,00.html)')
parser.add_argument('-o', dest = 'file', help = 'output file')
args = parser.parse_args()

# get page	
url = args.url
page = urllib2.urlopen(url).read()

# find rtmp url
link = (re.search('(rtmp%3A%2F%2F((?!%22).)*)%22',page))
if link is None: 
	print "Clip not found!"
	exit()
link = urllib2.unquote(link.group(1)) 

# grab video
if args.file is None:
	filename = os.path.basename(link)
else:
	filename = args.file
print ("Download: " + link)
os.system('rtmpdump -r ' + link + " -o " + filename)
