#!/usr/bin/python
#-*- coding: utf-8 -*-
import cgi, cgitb
from sqlalchemy import create_engine
from pandas import read_sql
cgitb.enable()
form = cgi.FieldStorage()
email = form.getvalue('email')
password = form.getvalue('password')

print "Content-type:text/html\r\n"
conn = create_engine('mysql://shopping_mall:shopping_mall@localhost/shopping_mall?charset=utf8')
df = read_sql("select 암호, 이름 from 회원 where 이메일 = '" + email + "';", conn)
if df[u'암호'][0] == password: print "logged in as " + email;
else: print 'log in failed'    
