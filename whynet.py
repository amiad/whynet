#!/usr/bin/python2
import sys, urllib2, os, re

url = sys.argv[1]
page = urllib2.urlopen(url).read()

link = (re.search('(rtmp%3A%2F%2F((?!%22).)*)%22',page))
if link is None: 
	print "Clip not found!"
	exit()
link = urllib2.unquote(link.group(1)) 
filename = os.path.basename(link)
print ("Download: " + link)
os.system('rtmpdump -r ' + link + " -o " + filename)
