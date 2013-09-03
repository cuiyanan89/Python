#!/usr/bin/python
#encoding=utf-8
import urllib2
import re
def geturl_list(url):
    urls = []
    try:
        html = urllib2.urlopen(url,timeout=9)
        text = html.read()
        urls_ex = re.findall(r'<a href="(http://.*?)"',text)
        for u in urls_ex:
            if u.find(url.split('/')[2])==-1:
                urls.append(u)
                print urls
    except:
        pass
    return urls

def deep_search(url_list):
    deep = 0 
    while deep < 20 and len(url_list) != 0:
        deep += 1
        print deep
        url = url_list.pop()
        urls = geturl_list(url)
        if len(urls) > 0 :
            url_list.append(url)
            url_list.extend(urls)
    return url_list

def main():
    url_list = ['http://www.cnblogs.com/']
    try:
        file = open('urllistfromcnbeta.txt','w')
        for url in deep_search(url_list):
            file.write(url+'\n')
        file.close()
    except:
        pass

if __name__=="__main__":
    main()

