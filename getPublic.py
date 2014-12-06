# -*- coding: utf-8 -*-
import requests
import re
from bs4 import BeautifulSoup
import time


payload = {'cb':'sogou.weixin.gzhcb',
		   'openid': 'oIWsFtwMeHKlgc8U6rPtQWR3AOTI',
		   'page': '1'}

r = requests.get('http://weixin.sogou.com/gzhjs',params=payload)
ava_urls=re.findall(r'mp.weixin.qq.com/s(.*?)]'.decode('utf-8').encode('utf-8'), r.content)
for ava_url in ava_urls:
	ava_url='http://mp.weixin.qq.com/s'+ava_url
	article=requests.get(ava_url)
	#print article.text
	#ava_contents=re.findall('<span style="font-size: 14px;">(.*?)</span>'.decode('utf-8').encode('utf-8'), article.text)
	#for ava_content in ava_contents:
	#	print ava_content
	#<span style="font-size: 14px;"> #</span>
	soup = BeautifulSoup(article.text)
	print(soup.title.string)
	js_content=soup.find_all(id="js_content")
	#print str(js_content).decode('utf-8').encode('gbk')
	contents=re.sub(r"<[^>]*>".decode('utf-8').encode('utf-8'), '',str(js_content))
	print contents
	print 'done'
	#for content in contents:
	#	print content
	#"<[^>]*>"
	#print soup
	#print(soup.findAll(['a','p','font']))	
	#time.sleep(2)