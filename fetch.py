import pymysql
tup=(('','Hyatt Regency','9','Aiport Road','Mumbai','India'),
('','The Oberoi','4','M.G. Road','Bangalore','India'),
('','The Leela Palace','6','Old Airport Road','Bangalore','India'),
        ('','ITC Gardenia','5','Ashok Nagar','Bangalore','India'),
        ('','Four Seasons Hotel Bengaluru at Embassy ONE','7','Bellary Road','Bangalore','India'))
conn=pymysql.Connect(host="localhost", user="root", passwd="", database="hotels")
cursor=conn.cursor()
for t in tup:
    cursor.execute(t)
conn.commit()
conn.close()
print(done)
