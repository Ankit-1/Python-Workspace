import sqlite3 as sq
conn = sq.connect("courses.db")
cursor=conn.cursor()
course=("34611","Non linear Signal Processing",10)
cursor.execute("INSERT INTO courses VALUES (?,?,?);",course)

conn.commit()
conn.close()