import sqlite3
con = sqlite3.connect('application.db')

cur = con.cursor()

# create table
cur.execute('''CREATE TABLE blogs 
            (id TEXT NOT NULL PRIMARY KEY, date TEXT, title TEXT, content TEXT, public INTEGER)''')

# Insert a few rows of data
cur.execute("INSERT INTO blogs VALUES('first-blog', '2021-03-07', 'My first blog', 'Some Content', 1)")
cur.execute("INSERT INTO blogs VALUES('private-blog', '2021-03-07', 'Secret blog', 'This is a secret', 0)")

# Save (commit) the changes
con.commit()

# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they would be lost.
con.close()