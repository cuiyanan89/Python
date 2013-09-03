#!/usr/bin/python
#encoding=utf-8
import urllib
import re
import os 
from sys import argv

def jpg_download(url,down_dir):
    html = urllib.urlopen(url).read()
    jpgurl = re.findall(r'src="(http://.*?\.jpg)" pic',html)
    if not os.path.exists(down_dir):
        os.mkdir(down_dir)
        os.system('/bin/chmod 777 -R %s'%down_dir)
    for jpg in jpgurl:
        file_name = down_dir+'%s'%jpg.split('/')[-1]
        if not os.path.isfile(file_name):
            urllib.urlretrieve(jpg,file_name)
            print jpg
def next_page(url):
    html_head = url.split('/')
    del html_head[-1]
    head =  '/'.join(html_head)
    html = urllib.urlopen(url).read()
    next_url = re.findall(r'<a href="/p/(\d+?\?pn=\d*)">',html)
    page_url = []
    for i in next_url:
        i = head + '/' +i 
        if i not in page_url:
            page_url.append(i)
            print page_url
    return page_url

if __name__ == '__main__':
    script,url = argv
    down_dir = r'/csvt/n12/python_note/image/'
    for page_url in next_page(url):
        jpg_download(page_url,down_dir)
