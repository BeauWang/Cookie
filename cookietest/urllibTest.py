# -*- coding:utf-8 -*-

from urllib import request
import urllib
import http.cookiejar

cookie = http.cookiejar.LWPCookieJar()
handle = request.HTTPCookieProcessor(cookie)
opener = request.build_opener(handle,request.HTTPHandler)
request.install_opener(opener)
response = request.urlopen(r"http://aaa2.nwsuaf.edu.cn:8080/selfservice/")

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:14.0) Gecko/20100101 Firefox/14.0.1',
           'Referer':r"http://aaa2.nwsuaf.edu.cn:8080/selfservice/"}
values = {'username' : '2013013280',  'password' : '06514X'}
data = urllib.parse.urlencode(values).encode('utf-8')
req = request.Request(r"http://aaa2.nwsuaf.edu.cn:8080/selfservice/",data,headers)
print(req)
response = request.urlopen(req)
text = response.read()
print(text)
f_obj = open('dontkonw.html','wb')
f_obj.write(text)
print('succeed')
# response = opener.open(r"http:// aaa2.nwsuaf.edu.cn:8080/selfservice/")
for item in cookie:
    print('name = ' +item.name)
    print('value = ' +item.value)
print(response.read())