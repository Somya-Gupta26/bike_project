import mysql.connector as mc

# Connect to MySQL database
conn = mc.connect(
    host='localhost',
    user='root',
    password='somya2657',
    database='Bike',
    charset='utf8' 
)
if(conn.is_connected()):
    print("Connection Established")
else:
    print("No Connection")

query_to_create_table = """
CREATE TABLE IF NOT EXISTS bikeData (
    brand VARCHAR(40),
    kms_driven INT,
    owner INT,
    age INT,
    power INT,
    predicted_price INT
)
"""

cur = conn.cursor() 
cur.execute(query_to_create_table) 
print("Your database and table are created")
cur.close()
conn.close()








