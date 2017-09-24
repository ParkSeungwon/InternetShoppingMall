#!/usr/bin/python
import cgi, os, cgitb, logging
import sqlalchemy as sql
import pandas as pd

cgitb.enable()
form = cgi.FieldStorage()
f = form['file']
name = form.getvalue('goods')
desc = form.getvalue('desc')
email = ''
#logging.basicConfig(filename='/tmp/log', level=logging.DEBUG)
#logging.info(name)
#if os.environ.has_key('HTTP_COOKIE'):
#    for cookie in map(strip, split(os.environ['HTTP_COOKIE'], ';')):
#        logging.info(cookie);
#        (key, value ) = split(cookie, '=');
#        if key == "email": email = value
#conn = create_engine('mysql://shopping_mall:shopping_mall@localhost/shopping_mall?charset=utf8')
#df = pd.read_sql(u"insert into 상품 (판매자, 상품정보, 상품명) values ('" + email + "', '" + desc + "', '" + name + "'); select last_insert_id();")
#logging.info(str(df.loc[0][0]));
#if f.filename:
#    open('/var/lib/tomcat8/webapps/In/image/'+str(df.loc[0][0]), 'wb').write(f.file.read())
print "Content-Type: text/html\r\n"
print "<html> <body> <p>uploaded %s </p> </body> </html>" % desc
