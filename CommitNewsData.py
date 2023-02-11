import psycopg2
import json
import sys

name = sys.argv[1]


conn = psycopg2.connect(
    host='db-stock-data.c0iscncut9ja.us-east-1.rds.amazonaws.com',
    database='mydb',
    port="5432",
    user="sergiocxz",
    password="8839Sanchez")
conn.autocommit = True

cur = conn.cursor()
cur.execute('TRUNCATE TABLE ' + name + '_news')

#cur.execute("create table %s_news (title VARCHAR(255), image VARCHAR(255), site VARCHAR(255), text VARCHAR(255), url VARCHAR(255)) ;" % name)
#records = cur.fetchall()
#print(records)



f = open('%s-news.json' % name)
data = json.load(f)

sTitle = ''
sImage = ''
sSite = ''
sText = ''
sURL = ''
x = 0
while x < 5:
    sTitle = json.dumps(data[x]['title'])
    sImage = json.dumps(data[x]['image'])
    sSite = json.dumps(data[x]['site'])
    sText = json.dumps(data[x]['text'])
    sURL = json.dumps(data[x]['url'])
    
    cur.execute('INSERT INTO ' + name + '_news (title, image, site, text, url) VALUES (%s, %s, %s, %s, %s);', (sTitle, sImage, sSite, sText, sURL) )
    print(sTitle, sImage, sSite, sText, sURL)
    x += 1

f.close()