#! /usr/bin/env python 
# -*-encode utf-8-*-
# request_task.py
import urllib,urllib2
import hmac
from insert_a_task import insert_a_task
import re
import os
import random 
from confirm  import confirm
from send_result import get_and_send_result
#from wyportmap.wyportmap import *

import ConfigParser
cf = ConfigParser.ConfigParser()
cf.read("./fireEye.conf")

def request_task():
# signature and communication
	key =cf.get("current","key_signature")   #'123456'
	msg = str(random.uniform(1,100))
	sign = hmac.new(key,msg).hexdigest()
	#url = 'http://localhost/test999.php'
	url = cf.get("current","url_request")# 'http://wtf.zbj.com/index.php?m=index&c=tools&a=scanport'
	values = {'msg':msg,'sign':sign}
	data = urllib.urlencode(values)
	req =  urllib2.Request(url,data)
	res = urllib2.urlopen(req).read()
	b = re.findall('\n\n(.*?)\n\n',res)
	print 'response form web:' +res
#	print 'len(b) = ' +str(len(b))
#	print  b
	if res == 'none':
		print 'no task is running,waiting for task'
	elif b[2] != 'none':
		insert_a_task(b[0],'0')
		confirm(b[0])
		path = cf.get("current","root_path") + 'wyportmap/wyportmap.py  '
		cmd = 'python '+' ' +  path + ' '+  b[1] +' ' + b[0] + ' ' + b[2]
		os.system(cmd)
		get_and_send_result(b[0])
#		delete_a_task(b[0])
	elif b[2] == 'none':
		insert_a_task(b[0],'0')
		confirm(b[0])
		cmd = 'python' + ' ' + path +' ' + b[1] +' ' + b[0]
		os.system(cmd)
		get_and_send_result(b[0])
#		delete_a_task(b[0])
	else:
		print 'the form of the task is not right,or other problem see request_task.py'
# select result from mysql and send to apache
	
