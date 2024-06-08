import sqlite3
connection=sqlite3.connect('user.db')
cursor=connection.cursor()

query="INSERT INTO  user (name ,password) VALUES ('admin','admin123');"

cursor.execute(query)
connection.commit()
connection.close()