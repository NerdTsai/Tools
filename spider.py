# -*- coding: <utf-8> -*-
#该py程序没有完成，暂且放这儿
import urllib2
import re
print 'Please input the URL:'
first_url = raw_input()
rule_url = '<[a|A].*?href=[\'\"]{0,1}([^>\'\"\/]*).*?>'
rule_title = '<title.*?>([\s\S]*).*?</title>'
rule_keys = '<meta.*?name="keywords" content=([^\<\>]*).*?>'
rule_desc = '<meta.*?name="description" content=([\s\S]*).*?>'
def get_url(url):
        url_content = urllib2.urlopen(url)
        url_text = url_content.read()
        match_url = re.compile(rule_url)
        match_title = re.compile(rule_title)
        match_keys = re.compile(rule_keys)
        match_desc = re.compile(rule_desc)
        con_url = match_url.findall(url_text)
        con_title = match_title.findall(url_text)
        con_keys = match_keys.findall(url_text)
        con_desc = match_desc.findall(url_text)
        print url+con_title[0]
        for text in con_url:
                 get_url(text)
get_url(first_url)
print "Over at all"
