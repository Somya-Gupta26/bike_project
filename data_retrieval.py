import mysql.connector as mc
conn = mc.connect(
    host='localhost',
    user='root',
    password='somya2657',
    database='Bike',
    charset='utf8'
)

cur = conn.cursor() 
query = "select * from bikeData"

cur.execute(query) 
for record in cur.fetchall():
    print(record) 

cur.close()
conn.close()