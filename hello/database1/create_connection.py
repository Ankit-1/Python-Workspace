import sqlite3 as sq
conn = sq.connect("courses.db")
cursor=conn.cursor()
# cursor.execute("""Create Table course(number INTEGER PRIMARY KEY,
#                     name text, ects real);""")
cursor.execute("""INSERT INTO course VALUES ("100","Python Programming",5)""")
conn.commit()
conn.close()