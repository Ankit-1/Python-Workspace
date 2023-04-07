import sqlite3 as sq
conn = sq.connect("courses.db")
cursor=conn.cursor()
cursor.execute("SELECT * FROM courses;")
# for g in cursor:
#     print(g)
    
# print("------------------------------------------------------")
# a=cursor.fetchall()
# print(a)
# a=cursor.fetchone()
# print(a)
cursor.execute("SELECT *FROM courses ORDER BY number LIMIT 4")
c=cursor.fetchall()
print(c)
conn.close()
