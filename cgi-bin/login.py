#!/usr/bin/python
import cgi
import sqlalchemy as sql
import pandas as pd

form = cgi.FieldStorage()
name = form.getvalue('username')
password = form.getvalue('password')
verify = form.getvalue('verify')
email = form.getvalue('email')
address = form.getvalue('address')
tel = form.getvalue('tel')

conn = sql.create_engine('mysql://shopping_mall:shopping_mall@localhost/shopping_mall?charset=utf8')
df = pd.read_sql('select 암호, 이름 from 회원 where 이메일 = ' + email + ';')
print "Content-type:text/html\r\n\r\n"
if df.size == 1: print "email already exist"
else if password != verify: print "password and verify does not match"
else:
    conn.execute('insert into 회원 values (' + email + ',' + name + ',' + password + ',' + address + ',' + tel + ', 1);')
    print '가입완료'    
    s = 'logged in as ' + df[u'이름'][0]
