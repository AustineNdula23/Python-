import socket

# Create a UDP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind the socket to a specific IP address and port number
server_ip = '127.0.0.1'
server_port = 12345
server_socket.bind((server_ip, server_port))

print("UDP Server is listening...")

while True:
    # Receive data from the client and the client address
    data, client_address = server_socket.recvfrom(1024)
    print(f"Received data from {client_address}: {data.decode()}")

    # Process the data (you can perform any required operations here)

    # Send a response back to the client
    response_data = "Hello, client! I received your message."
    server_socket.sendto(response_data.encode(), client_address)
