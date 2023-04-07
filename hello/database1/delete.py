import sqlite3 as sq
conn = sq.connect("courses.db")
cursor=conn.cursor()

# cursor.execute("SELECT *FROM courses WHERE number=? OR name=? OR ects=?",(2346,"value2","value3"))
cursor.execute("SELECT * FROM courses;")
a=cursor.fetchall()
print(a)

# cursor.execute("UPDATE courses SET name=?,ects=? WHERE number=?",('Nishant',56.90,34611))
# rows=cursor.fetchall()

cursor.execute("DELETE FROM courses WHERE number=?",(2346,))

conn.commit()

print('------------------------------------------------------------------------------------')

cursor.execute("SELECT * FROM courses;")
a=cursor.fetchall()
print(a)

conn.close()