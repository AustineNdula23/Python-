import socket

# Create a UDP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Set the server's IP address and port number
server_ip = '127.0.0.1'
server_port = 12345

# Send data to the server
message = "Hello, server! This is the client speaking."
client_socket.sendto(message.encode(), (server_ip, server_port))

# Receive the response from the server
response, server_address = client_socket.recvfrom(1024)
print(f"Received response from {server_address}: {response.decode()}")

# Close the socket
client_socket.close()
