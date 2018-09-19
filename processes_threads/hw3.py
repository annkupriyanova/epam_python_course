import socket
import os
import hashlib


def main_server_function(port: int = 8000, num_of_workers: int = 2):

    # Create a TCP/IP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Bind the socket to the port
    server_address = ('localhost', port)
    print('starting up on {} port {}'.format(*server_address))
    sock.bind(server_address)

    # Listen for incoming connections
    sock.listen(num_of_workers)

    while True:
        # Wait for a connection
        print('waiting for a connection')
        connection, client_address = sock.accept()
        try:
            child_pid = os.fork()
            if child_pid == 0:
                print('connection from', client_address, 'new process started', child_pid)

                data = connection.recv(16)
                if data:
                    print('received {!r}'.format(data))
                    print('sending data back to the client')
                    answer = factorial(int(data))
                    m = hashlib.md5()
                    m.update(bytes(str(answer), 'utf-8'))

                    connection.sendall(m.digest())
                else:
                    print('no data from', client_address)
                    break

        finally:
            # Clean up the connection
            connection.close()

    sock.close()


def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)


def client(number, port=8000):
    # Create a TCP/IP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect the socket to the port where the server is listening
    server_address = ('localhost', port)
    print('connecting to {} port {}'.format(*server_address))
    sock.connect(server_address)

    try:

        # Send data
        print(number)
        message = bytes(str(number), 'utf-8')
        print('sending {!r}'.format(message))
        sock.sendall(message)

        data = sock.recv(16)
        print('received {!r}'.format(data))

    finally:
        print('closing socket')
        sock.close()


if __name__ == '__main__':
    main_server_function()
