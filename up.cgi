#!/usr/bin/python
#-*- coding: utf-8 -*-
import cgi, os, cgitb, logging
import sqlalchemy as sql
import pandas as pd

cgitb.enable()
logging.basicConfig(filename='/tmp/log', level=logging.DEBUG)
form = cgi.FieldStorage()
f = form['file']
name = form.getvalue('goods')
desc = form.getvalue('desc')
email = ''
if os.environ.has_key('HTTP_COOKIE'):
    for cookie in os.environ['HTTP_COOKIE'].split( ';'):
        cookie = cookie.strip();
        key, value = cookie.split('=');
        if key == "email": 
            email = value;
            break;

remote = 'mysql://inzent:1q2w3e4r!@inzent.cyuky5umqyhf.ap-northeast-2.rds.amazonaws.com/inzent?charset=utf8'
local = 'mysql://shopping_mall:shopping_mall@localhost/shopping_mall?charset=utf8'
conn = create_engine(remote)
conn.execute(u"insert into 상품 (판매자, 상품정보, 상품명) values ('" + email + "', '" + unicode(desc,'utf8') + "', '" + unicode(name,'utf8') + "');")
df = pd.read_sql(u'select max(상품아이디) from 상품;', conn)

if f.filename:
    open('/var/lib/tomcat8/webapps/In/image/'+str(df.loc[0][0]), 'wb').write(f.file.read())
    print "Content-Type: text/html\r\n"
    print "<html> <body> <p>uploaded %s </p> </body> </html>" % email
