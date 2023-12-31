import sqlite3

# Create a SQL connection to our SQLite database
con = sqlite3.connect("instance/CrimeAnalysis.db")
cur = con.cursor()

# The result of a "cursor.execute" can be iterated over by row
for row in cur.execute('SELECT * FROM users'):
    print(row)

con.commit() 
# Be sure to close the connection
con.close()