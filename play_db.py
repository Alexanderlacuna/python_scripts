import sqlite3
conn = sqlite3.connect("chinook.db")
print(conn)

c = conn.cursor()
c.execute("select * from artists")


results = c.fetchone()
print(results)
commit = "4f73a3f024fc0dc74bbe4d8b02f0eb83b6516485"

hash ="02m6y74zxfh8349nvkrgg044ajl5b2di5nlxq9wjla17sf342zw4"