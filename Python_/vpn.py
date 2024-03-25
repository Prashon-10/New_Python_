import socket

def create_vpn_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 12345))
    server_socket.listen(1)
    print('VPN server is running on localhost:12345')

    while True:
        client_socket, client_address = server_socket.accept()
        print(f'New connection from {client_address[0]}:{client_address[1]}')

        # Handle client requests and send/receive data

        client_socket.close()

if __name__ == '__main__':
    create_vpn_server()