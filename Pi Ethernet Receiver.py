import socket

# Server configuration
HOST = ''  # Listen on all available interfaces
PORT = 12345  # Choose a port number

# Create a socket
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
    # Bind the socket to the host and port
    server_socket.bind((HOST, PORT))
    # Listen for incoming connections
    server_socket.listen()
    print('Server listening on port', PORT)
    # Accept incoming connection
    conn, addr = server_socket.accept()
    with conn:
        print('Connected by', addr)
        # Receive and print incoming messages
        while True:
            data = conn.recv(1024)
            if not data:
                break
            print('Received:', data.decode())
