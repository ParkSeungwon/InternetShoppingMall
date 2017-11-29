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
remote = 'mysql://inzent:1q2w3e4r!@inzent.cyuky5umqyhf.ap-northeast-2.rds.amazonaws.com/inzent?charset=utf8'
local = 'mysql://shopping_mall:shopping_mall@localhost/shopping_mall?charset=utf8'
conn = create_engine(remote)
df = read_sql_table(u'상품', conn)
df = df[df[u'상품정보'].str.contains(s) | df[u'상품명'].str.contains(s)]
y, x = df.shape
for i in range(y):
    for j in range(x):
        print df.iloc[i, j]
        print '$$separator$$'
    print '''<form action="https://www.paypal.com/cgi-bin/webscr" method="post" target="_top">
<input type="hidden" name="cmd" value="_s-xclick">
<input type="hidden" name="hosted_button_id" value="NZHZN3TMTTMNG">
<input type="image" src="https://www.paypalobjects.com/en_US/i/btn/btn_donateCC_LG.gif" border="0" name="submit" alt="PayPal - The safer, easier way to pay online!">
<img alt="" border="0" src="https://www.paypalobjects.com/en_US/i/scr/pixel.gif" width="1" height="1">
</form>$$separator$$'''
