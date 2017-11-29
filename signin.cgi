#!/usr/bin/python
#-*- coding: utf-8 -*-
import cgi
from sqlalchemy import create_engine
from pandas import read_sql
import cgitb
cgitb.enable()
form = cgi.FieldStorage()
name = form.getvalue('username')
password = form.getvalue('password')
verify = form.getvalue('verify')
email = form.getvalue('email')
address = form.getvalue('address')
tel = form.getvalue('tel')

print "Content-type:text/html\r\n"
print '<h2>hello cgi here</h2>' 
<<<<<<< HEAD
conn = create_engine('mysql://shopping_mall:shopping_mall@localhost/shopping_mall?charset=utf8')
=======
remote = 'mysql://inzent:1q2w3e4r!@inzent.cyuky5umqyhf.ap-northeast-2.rds.amazonaws.com/inzent?charset=utf8'
local = 'mysql://shopping_mall:shopping_mall@localhost/shopping_mall?charset=utf8'
conn = create_engine(remote)
>>>>>>> master
df = read_sql(u"select * from 회원 where 이메일 = '" + email + "';", conn)
if df.size > 0: 
    print "email already exist"
else:
    conn.execute(u"insert into 회원 values ('" + email + "','" + unicode(name, 'utf8') + "','" + password + "','" + unicode(address,'utf8') + "','" + tel + "', 1);")
    print '가입완료'    
