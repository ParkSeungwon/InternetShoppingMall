#!/usr/bin/python
#-*- coding: utf-8 -*-
import cgi, cgitb
from sqlalchemy import create_engine
from pandas import read_sql
cgitb.enable()
form = cgi.FieldStorage()
email = form.getvalue('email')
password = form.getvalue('password')

<<<<<<< HEAD
conn = create_engine('mysql://shopping_mall:shopping_mall@localhost/shopping_mall?charset=utf8')
=======
remote = 'mysql://inzent:1q2w3e4r!@inzent.cyuky5umqyhf.ap-northeast-2.rds.amazonaws.com/inzent?charset=utf8'
local = 'mysql://shopping_mall:shopping_mall@localhost/shopping_mall?charset=utf8'
conn = create_engine(remote)
>>>>>>> master
df = read_sql(u"select 암호, 이름 from 회원 where 이메일 = '" + email + "';", conn)
if df.size > 0 and df[u'암호'][0] == password: 
    print 'Set-Cookie:email=' + email + ';\r\n'
    print "logged in as " + email;
else: 
    print "Content-type:text/html\r\n"
    print 'log in failed'    
