import socket

# create a socket object
s = socket.socket()

# define the port on which you want to connect
port = 12345

# connect to the server on the specified port
s.connect(('127.0.0.1', port))

# send data to server
while True:
    message = input("Enter message to send to server: ")
    s.send(message.encode())
    data = s.recv(1024).decode()
    print('Received from server: ', data)

# close the connection
s.close()
