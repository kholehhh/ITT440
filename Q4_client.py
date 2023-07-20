# Ahmad Haziq Khalis bin Khairul Anuar 2021619528
# Client Code

import socket

def main():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_host = '192.168.137.128'
    server_port = 8888

    try:
        client_socket.connect((server_host, server_port))
        print("Connected to the QOTD server.")

        while True:
            reply = input("Press 'Enter' to get a quote or type 'exit' to quit: ")
            if reply.lower() == 'exit':
                break

            client_socket.send(b"quote")
            quote = client_socket.recv(2048).decode()
            print(f"Quote of the Day: {quote}")

    except ConnectionRefusedError:
        print("Connection to the QOTD server failed. Please ensure the server is running.")
    except KeyboardInterrupt:
        print("\nClient is closing...")
    finally:
        client_socket.close()

if __name__ == "__main__":
    main()


