import MySQLdb
db=MySQLdb.connect(host="localhost",user="root",passwd="",db="hotels")
cursor=db.cursor()
cursor.execute("""INSERT INTO oyo_customer (name) VALUES (%s)""",('your_name',))
db.commit()
cursor.close()
db.close()
