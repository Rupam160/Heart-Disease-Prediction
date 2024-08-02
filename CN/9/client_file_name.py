import socket

# Define the server address and port
server_address = ('localhost', 8080)

# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Message to be sent
message = "Hello from client"

# Send message to server
sock.sendto(message.encode(), server_address)
print("Hello message sent to server")

# Receive hello message from server
data, server = sock.recvfrom(1024)
print("Received message from server:", data.decode())

# Close the socket
sock.close()
