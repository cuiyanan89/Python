#!/usr/bin/python
#coding=utf-8
import urllib
import re
import os
import threading
from sys import argv

def jpg_Url(url):
    html = urllib.urlopen(url).read()
    jpg_re = r'src="(http://imgsrc.baidu.com/forum/.*?\.jpg)"'
    jpg_re = re.compile(jpg_re)
    url_list = jpg_re.findall(html)
    return url_list

def image_File():
    image_file = os.path.join(os.getcwd(),'image')
    if not os.path.exists(image_file):
        os.mkdir(image_file)
    os.chdir(image_file)
    
def jpg_Download(url):
    jpgname = os.path.join(os.getcwd(),url.split('/')[-1])
    urllib.urlretrieve(url,jpgname)
    print jpgname

def main():
    script,url = argv
    image_File()
    url_list = jpg_Url(url)
    for jpgurl in url_list:
        jpgthread = threading.Thread(target = jpg_Download,args=(jpgurl,))
        jpgthread.start()

if __name__=='__main__':
    main()
