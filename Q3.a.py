# Ahmad Haziq Khalis bin Khairul Anuar 2021619528
# Write a server program that will convert received pressure in bar to atmosphere-standard

import socket

def bar_to_atmosphere(bar):
    return bar * 0.986923

def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_host = '192.168.137.128'
    server_port = 8443

    server_socket.bind((server_host, server_port))
    server_socket.listen(1)
    print("Server is listening for connections...")

    while True:
        try:
            connection, address = server_socket.accept()
            print(f"Connection established with {address}")

            while True:
                data = connection.recv(1024)
                if not data:
                    break

                try:
                    bar_value = float(data.decode())
                    atmosphere_value = bar_to_atmosphere(bar_value)
                    connection.send(str(atmosphere_value).encode())

                except ValueError:
                    connection.send(b"Invalid pressure value")

            connection.close()

        except KeyboardInterrupt:
            print("\nServer is shutting down...")
            break

    server_socket.close()

if __name__ == "__main__":
    main()

