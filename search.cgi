#!/usr/bin/python
#-*- coding: utf-8 -*-
import cgi
from sqlalchemy import create_engine
from pandas import read_sql
import cgitb
cgitb.enable()
form = cgi.FieldStorage()
s = form.getvalue('search')

print "Content-type:text/html\r\n"
conn = create_engine('mysql://shopping_mall:shopping_mall@localhost/shopping_mall?charset=utf8')
df = read_sql_table(u'상품', conn)
df = df[df[u'상품정보'].str.contains(s) | df[u'상품명'].str.contains(s)]
content_ = "<table bgcolor='#005500' border='1'>";
y, x = df.shape
for i in range(y):
    content_ += "<tr><td><img src='image/" + df.iloc[y, 0];
    content_ += "' height=300 width=300 /></td>";
    for(j in range(x-1): content_ += "<td>" + df.iloc[y, j+1] + "</td>";
    content_ += "</tr>";
}
content_ += "</table>";
print content_
