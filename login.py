import sqlite3
import hashlib
#connect to the SQLite database name 'user.db'
#if the database does not exist it wil be created
conn = sqlite3.connect("user.db")
cur = conn.cursor() #this creates a cursor object to interact with a databse
cur.execute( """
CREATE TABLE IF NOT EXISTS userdata(
    id INTEGER PRIMARY KEY,
    username VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL
)
"""
)
#Define four sets of usernames and passwords
#Hash the passwords using Sha-256 for security purposes
username1, password1 = "mike123", hashlib.sha256("mikepassword".encode()).hexdigest()
username2, password2 = "mark", hashlib.sha256("markpassword".encode()).hexdigest()
username3, password3 = "johncole", hashlib.sha256("jcpassword".encode()).hexdigest()
username4, password4 = "alpha", hashlib.sha256("alphapassword".encode()).hexdigest()
#Insert these usernames and hashed passwords into the 'userdata' table
cur.execute("INSERT INTO userdata (username, password) VALUES (?,?)", (username1, password1))
cur.execute("INSERT INTO userdata (username, password) VALUES (?,?)", (username2, password2))
cur.execute("INSERT INTO userdata (username, password) VALUES (?,?)", (username3, password3))
cur.execute("INSERT INTO userdata (username, password) VALUES (?,?)", (username4, password4))
#commit changes
conn.commit()









