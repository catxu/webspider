# Purpose: Capture all the search suggestion key word of Baidu.
# Author: catxu
# Date: 2016-06-27
# Interpreter: Python 3.5

#https://sp0.baidu.com/5a1Fazu8AA54nxGko9WTAnF6hhy/su?wd=c&json=1&p=3&sid=19637_1426_20318_13290_17943_20389_19689_20417_20467_15297_11963&req=2&csor=0&cb=jQuery110207020267045802215_1467035348770&_=1467035348774

import urllib
import urllib.request

keyWord = urllib.parse.quote('cd')
#print(keyWord)
url = 'https://sp0.baidu.com/5a1Fazu8AA54nxGko9WTAnF6hhy/su?wd=' + keyWord + '&json=1&p=3&sid=19637_1426_20318_13290_17943_20389_19689_20417_20467_15297_11963&req=2&csor=0&cb=jQuery110207020267045802215_1467035348770&_=1467035348774'

headers = {
    "GET":url,
    "Host":"sp0.baidu.com",
    "Referer":"https://www.baidu.com/",
    "User-Agent":"Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36",
}

req = urllib.request.Request('https://www.baidu.com/')

for key in headers:
	req.add_header(key, headers[key])

html = urllib.request.urlopen(req).read()
print(html)
