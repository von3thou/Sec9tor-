import sqlite3
import hashlib
import socket
import threading
def handle_connection(c):
    try:
        print("Client Connected")
        #Send a prompt to the client asking for the username
        c.send("Username:".encode())
        # Recieve the username from the client
        username = c.recv(1024).decode().strip()
        print(f"Recieved username:{username}")
        #Send a prompt to the client asking for the password
        c.send("Password: ".encode())
        #Recieve the password from the client
        password = c.recv(1024).decode().strip()
        print(f"Recoeved password (pre-hash): {password}")
        #Hash the password using Sha-256 for security
        password = hashlib.sha256(password.encode()).hexdigest()
        print(f"Hashed password: {password}")
        #Connect to the Sqlite databse
        conn = sqlite3.connect("user.db")
        cur = conn.cursor()
        #Check if the username and hashed password match any entry in the databse
        cur.execute("SELECT * FROM userdata WHERE username = ? AND password = ?", (username, password))
        # If a match is found, send a success message to the client
        if cur.fetchone() is not None:
            c.send ("Login Successfully!".encode())
            print ("Login successful")
# If no match is found, send a failure message to the client
        else:
            c.send ("Login Failed!".encode())
            print ("Login Failed!")
#Close the database connection
        conn.close()
    except Exception as e:
        #If an error ocurs, print the error and send an error message to the client
        print(f"Error: {str(e)}")
        c.send(f"Error: {str(e)}".encode())
    finally:
        #close the client connection
        c.close()
# Create a socket object for the server
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Bind the server to localhost on port 3333
server.bind(("localhost", 3333))
# Start listening for incoming connections
server.listen()
print("Server started on port 3333...")
while True:
# Accept an incoming clicht connection
    client, addr = server.accept()
# Handle the client connection in a new thread
    threading.Thread(target=handle_connection, args=(client,)).start()











