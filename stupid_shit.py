#SQLITE? waste of everyone's fuckking time jwessus christ waht is this fucking moron thinking?!?!?
import sqlite3

#Esatblish a conneciton and a server
connection = sqlite3.connect("data.db")
cursor = connection.cursor()

#quest data
cursor.execute("SELECT * FROM events")
rows = cursor.fetchall()
print(rows)


#inssrt new row

# new_rows = [('Gargle blah','Music City','2055.05.04'),
#             ('Noise makesr','Lexington','2042.12.01')]
#
# cursor.executemany("INSERT INTO events VALUES(?,?,?)", new_rows)
# connection.commit()

