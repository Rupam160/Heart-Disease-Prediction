import socket

# Define the server address and port
server_address = ('localhost', 8080)

# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind the socket to the server address
sock.bind(server_address)

while True:
    print("Server is waiting to receive message...")
    
    # Receive message from client
    data, address = sock.recvfrom(1024)
    print("Received message:", data.decode())
    
    # Send hello message to client
    message = "Hello from server"
    sock.sendto(message.encode(), address)
    print("Hello message sent to", address)
