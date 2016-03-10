# -*-encode utf-8-*-
#post.py
# confirm that I have receved task,and send to server 
import urllib,urllib2
import hmac
from insert_a_task import insert_a_task
import re
import os
import random 

import ConfigParser
cf = ConfigParser.ConfigParser()
cf.read("./fireEye.conf")



def confirm(qid):
# signature and communication
	key = cf.get("current","key_signature")   #'123456'
	msg = str(random.uniform(1,100))
	sign = hmac.new(key,msg).hexdigest()
	#url = 'http://localhost/test999.php'
	url = cf.get("current","url_confirm")   # 'http://wtf.zbj.com/index.php?m=index&c=tools&a=sureport'

	values = {'msg':msg,'sign':sign,'qid':qid}
	data = urllib.urlencode(values)
	req =  urllib2.Request(url,data)
	res = urllib2.urlopen(req).read()
	return res

















