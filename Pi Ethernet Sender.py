import socket

# Server address and port
SERVER_HOST = 'server_ip_address'  # Replace with the IP address of the server Raspberry Pi
SERVER_PORT = 12345  # Same port number used by the server

# Message to send
message = "Hello from client!"

# Create a socket
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
    # Connect to the server
    client_socket.connect((SERVER_HOST, SERVER_PORT))
    # Send the message
    client_socket.sendall(message.encode())
    print('Message sent to server:', message)
