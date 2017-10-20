#!/usr/bin/python
#-*- coding: utf-8 -*-
import cgi
from sqlalchemy import create_engine
from pandas import read_sql_table
import cgitb
cgitb.enable()
form = cgi.FieldStorage()
s = unicode(form.getvalue('search'), 'utf8')

print "Content-type:text/html\r\n"
conn = create_engine('mysql://shopping_mall:shopping_mall@localhost/shopping_mall?charset=utf8')
df = read_sql_table(u'상품', conn)
df = df[df[u'상품정보'].str.contains(s) | df[u'상품명'].str.contains(s)]
y, x = df.shape
for i in range(y):
    for j in range(x):
        print df.iloc[i, j]
        print '$$separator$$'
