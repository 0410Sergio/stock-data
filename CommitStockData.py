import psycopg2
import json
import sys
from datetime import datetime

name = sys.argv[1]
#name = 'AAPL'

conn = psycopg2.connect(
    host='db-stock-data.c0iscncut9ja.us-east-1.rds.amazonaws.com',
    database='mydb',
    port="5432",
    user="sergiocxz",
    password="8839Sanchez")
conn.autocommit = True

cur = conn.cursor()
cur.execute('TRUNCATE TABLE ' + name + '_stock')

#cur.execute("create table %s_stock (date VARCHAR(255), price NUMERIC(6, 2), change NUMERIC(5, 2), changePercent NUMERIC(5, 2));" % name)
#records = cur.fetchall()
#print(records)



f = open('%s-stock.json' % name)
data = json.load(f)

sDate = ''
sPrice = ''
sChange = ''
sChangePercent = ''
x = 0
while x < 31:
    try: sDate = json.dumps(data['historical'][x]['date'], indent=4).replace('"', "")
    except: sDate = datetime.today().strftime('%Y-%m-%d')

    try: sPrice = json.dumps(data['historical'][x]['close'], indent=4)
    except: sPrice = json.dumps(data['historical'][x]['price'], indent=4)

    try: sChange = json.dumps(data['historical'][x]['change'], indent=4)
    except: sChange = 0

    try: sChangePercent = json.dumps(data['historical'][x]['changePercent'], indent=4)
    except: sChangePercent = 0

    try: data_formatted = json.dumps(data['historical'][x]['date'], indent=4)
    except: data_formatted = 0

    cur.execute('INSERT INTO ' + name + '_stock (date, price, change, changePercent) VALUES (%s, %s, %s, %s);', (sDate, sPrice, sChange, sChangePercent) )
    print(sDate, sPrice, sChange, sChangePercent)
    x += 1

#print(data_formatted)
f.close()