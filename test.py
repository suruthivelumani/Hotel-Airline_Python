import mysql.connector
conn=mysql.connector.connect(host="localhost", port="3307", user="root", password="", database="sampledb")
cursor=conn.cursor()
cursor.execute("select * from sample")
records=cursor.fetchall()
for row in records:
    print("ID:",row[0])
    print("First Name:",row[1])
    print("Last Name:",row[2])
    print("username:",row[3])
cursor.close()
conn.close()