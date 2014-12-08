# -*- coding: utf-8 -*-
import requests
import re
from bs4 import BeautifulSoup
import time
from mydb import Ganhuo


myweixin=Ganhuo()
public_dict={'oIWsFtwMeHKlgc8U6rPtQWR3AOTI':'左林右狸',
			 'oIWsFt0iI0FgrJ7s2-WLWjnka5OA':'豆瓣FM',
			 'oIWsFt-Yeb1hMiyk9MSpENdGTI7w':'PingWest中文网',
			 'oIWsFt-NQJJTI1l_HJBI-iEy3qbg':'36氪',
			 'oIWsFt8cEn8DvPhPck_8BgwOPRqw':'创业那些坑',
			 'oIWsFt8-Y1Le-NB8b0uP56xN-8jI':'大家',
			 'oIWsFtw2V9YRrYiR3gx7crd2XHmo':'壹读',
			 'oIWsFt9xe_3et8XZtNvvlDPo0hgk':'北京创客空间',
			 'oIWsFtzVAoAfGkflqIHqXiX6yrbQ':'刺猬公社',
			 'oIWsFt44sg-dOoMHvJoqt26HnfKM':'程序员的那些事',
			 'oIWsFt7OVLOudxrGznZ_bMihIwKE':'南方周末',
			 'oIWsFt0I3Dwtk5Ml0KnJcf3fz_Ao':'澎湃新闻',
			 'oIWsFt86MuAacbPGA3TM1glwaTp4':'果壳网',
			 'oIWsFt3nvJ2jaaxm9UOB_LUos02k':'简书',
			 'oIWsFt5HJEgGlbxXAB2hBcmwjQho':'知乎日报',	
			 'oIWsFtwVm9IdlPUp7LB_gVJdWZiQ':'一个',
			 'oIWsFt6PH59ZxXbHnRYKkvLIgcCc':'共识网',
}

payload = {'cb':'sogou.weixin.gzhcb',
		   'openid': 'oIWsFtwMeHKlgc8U6rPtQWR3AOTI',
		   'page': '1'}
index=0

for key in public_dict:
	index=index+1
	payload['openid']=key
	r = requests.get('http://weixin.sogou.com/gzhjs',params=payload)
	ava_urls=re.findall(r'mp.weixin.qq.com/s(.*?)]'.decode('utf-8').encode('utf-8'), r.content)
	for ava_url in ava_urls:
		ava_url='http://mp.weixin.qq.com/s'+ava_url
		article=requests.get(ava_url)
		soup = BeautifulSoup(article.text)
		
		js_content=soup.find_all(id="js_content")		
		contents=re.sub(r"<[^>]*>".decode('utf-8').encode('utf-8'), '\n',str(js_content).decode('utf-8').encode('utf-8','ignore'))#去除注解符
		contents=re.sub('\n\n*'.decode('utf-8').encode('utf-8'), '\n',str(contents))#撸成只有一个回车

		post_date=soup.find_all(id='post-date')
		date=re.sub(r"<[^>]*>".decode('utf-8').encode('utf-8'), '',str(post_date))

		#activity_name=soup.find_all(id='activity-name')
		title=soup.title
		#title=title.replace('<title>','')
		#title=title.replace('</title>','')
		#id="activity-name"
		myweixin.insert_data(title,date,public_dict[key],str(contents))
		#print contents,date,title
		#print 'done:',public_dict[key].decode('utf-8').encode('gbk','ignore'),index
#