# Ahmad Haziq Khalis bin Khairul Anuar 2021619528
# Server Code

import socket
import random
import threading

QUOTES = [
    "Don't be afraid of failure. Learn from it and keep going. Persistence is the key to success. - BJ Habibie",
    "As long as we remain united, we can achieve greatness and overcome any challenges that come our way. - BJ Habibie",
    "Education is the foundation of progress and development for a nation. - BJ Habibie",
    "Learn to be tolerant and embrace diversity, for that is the essence of humanity. - Buya Hamka",
    "The beauty of knowledge lies not in acquiring it, but in sharing it for the betterment of society. - Buya Hamka",
    "A kind word and a smile can brighten anyone's day. - Buya Hamka",
    "Leadership is about setting a vision, making tough decisions, and working tirelessly to achieve the desired outcomes. - Mahathir Mohamad",
    "A nation's wealth is not only in its resources but also in the potential and capabilities of its people. - Mahathir Mohamad",
    "The future belongs to those who invest in education and innovation. - Mahathir Mohamad"
    "The journey of a thousand miles begins with one step. - Lao Tzu",
    "The only thing standing between you and your goal is the story you keep telling yourself as to why you can't achieve it. - Jordan Belfort",
    "The only place where success comes before work is in the dictionary. - Vidal Sassoon",
    "It's not about ideas. It's about making ideas happen. - Scott Belsky",
    "Your time is limited, don't waste it living someone else's life. - Steve Jobs",
    "The biggest risk is not taking any risk. In a world that is changing quickly, the only strategy that is guaranteed to fail is not taking risks. - Mark Zuckerberg",
    "The only thing we have to fear is fear itself. - Franklin D. Roosevelt",
    "Success is not in what you have, but who you are. - Bo Bennett",
    "You miss 100% of the shots you don't take. - Wayne Gretzky",
    "The best time to plant a tree was 20 years ago. The second best time is now. - Chinese Proverb",
    "The only true wisdom is in knowing you know nothing. - Socrates"
]

def get_random_quote():
    return random.choice(QUOTES)

def handle_client(connection, address):
    print(f"Connected to {address}")

    try:
        while True:
            request = connection.recv(1024).decode()
            if request.lower() == "quote":
                quote = get_random_quote()
                connection.send(quote.encode())
            else:
                break

    except Exception as e:
        print(f"Error: {e}")

    finally:
        connection.close()
        print(f"Connection with {address} closed")

def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_host = '192.168.137.128'
    server_port = 8888

    server_socket.bind((server_host, server_port))
    server_socket.listen(5)
    print("QOTD Server is listening for connections...")

    try:
        while True:
            connection, address = server_socket.accept()
            client_thread = threading.Thread(target=handle_client, args=(connection, address))
            client_thread.start()

    except KeyboardInterrupt:
        print("\nQOTD Server is shutting down...")
        server_socket.close()

if __name__ == "__main__":
    main()
