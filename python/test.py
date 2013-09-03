#!/usr/bin/python
#encoding=utf-8
import urllib2
import re
import os
from sys import argv

def search(url,deep):
    print url
    if deep == 0:
        return 0
    url_list = []
    html = urllib2.urlopen(url,timeout=5).read()
    urls = re.findall(r'<a href="(http://.*?)"',html)
    search(urls[-1],deep-1)

if __name__=='__main__':
    script,url = argv
    list_search = search(url,10)
    
