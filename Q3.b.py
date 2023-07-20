import socket

def get_server_info():
    while True:
        try:
            server_host = input("Enter server IP address (or 'exit' to quit): ")
            if server_host.lower() == 'exit':
                return None, None

            server_port = input("Enter server port: ")
            try:
                server_port = int(server_port)
                return server_host, server_port
            except ValueError:
                print("Invalid port number. Please enter a valid integer port.")
        except KeyboardInterrupt:
            print("\nClient is closing...")
            return None, None

def get_user_input():
    while True:
        bar_input = input("Enter pressure in bar (or 'exit' to quit): ")
        if bar_input.lower() == 'exit':
            return None
        try:
            bar_value = float(bar_input)
            return bar_value
        except ValueError:
            print("Invalid input. Please enter a valid pressure value.")

def main():
    while True:
        server_host, server_port = get_server_info()
        if server_host is None or server_port is None:
            break

        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        try:
            client_socket.connect((server_host, server_port))
            print("Connected to the server.")

            while True:
                bar_value = get_user_input()
                if bar_value is None:
                    break

                client_socket.send(str(bar_value).encode())

                atmosphere_value = client_socket.recv(1024).decode()
                print(f"Atmosphere-standard value: {atmosphere_value} atm\n")

        except ConnectionRefusedError:
            print("Connection to the server failed. Please ensure the server is running.")
        except KeyboardInterrupt:
            print("\nClient is closing...")
        finally:
            client_socket.close()

if __name__ == "__main__":
    main()
