import socket

# define the port on which you want to connect
port = 12345

# create a socket object
s = socket.socket()

# bind to the port
s.bind(('localhost', port))

# put the socket into listening mode
s.listen(5)
print("Server is listening...")

# accept connection from client
conn, addr = s.accept()
print('Connected to', addr)

# receive data from the client
while True:
    data = conn.recv(1024).decode()
    if not data:
        break
    print("From connected user: " + data)
    conn.send(data.encode())

# close the connection
conn.close()
