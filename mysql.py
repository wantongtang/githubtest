# mysql.py
# connect mysql database

import MySQLdb

import ConfigParser
cf = ConfigParser.ConfigParser()
cf.read("./fireEye.conf")


def do_mysql_operate(str):
	try:
		conn = MySQLdb.connect(host = cf.get("db","db_host"),user = cf.get("db","db_user"),passwd  = cf.get("db","db_pass"),db = cf.get("db","db_name_task"),port =  cf.get("db","db_port"))
		cur = conn.cursor()

		count = cur.execute(str)
		conn.commit()
		cur.close()
		conn.close()
		return count
	except MySQLdb.Error,e:
		print "mysql error %d:%s" %(e.args[0],e.args[1])
		return 0
