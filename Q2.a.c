// Ahmad Haziq Khalis bin Khairul Anuar 2021619528
// Question 2 - Write a server program to pass one random number ranging from 100 to 999

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>
#include <unistd.h>
#include <arpa/inet.h>

#define SERVER_PORT 8080

int main() {
    int sockfd, newsockfd;
    struct sockaddr_in server_addr, client_addr;
    socklen_t client_addr_len = sizeof(client_addr);
    char buffer[4]; // Buffer to store the random number (3 digits + null terminator)

    // Create a TCP socket
    sockfd = socket(AF_INET, SOCK_STREAM, 0);
    if (sockfd < 0) {
        perror("Error creating socket");
        return 1;
    }

    // Configure server address
    memset(&server_addr, 0, sizeof(server_addr));
    server_addr.sin_family = AF_INET;
    server_addr.sin_addr.s_addr = INADDR_ANY;
    server_addr.sin_port = htons(SERVER_PORT);

    // Bind the socket to the server address
    if (bind(sockfd, (struct sockaddr*)&server_addr, sizeof(server_addr)) < 0) {
        perror("Bind failed");
        close(sockfd);
        return 1;
    }

    // Listen for incoming connections
    if (listen(sockfd, 1) < 0) {
        perror("Listen failed");
        close(sockfd);
        return 1;
    }

    printf("Server is listening for incoming connections...\n");

    // Accept a client connection
    newsockfd = accept(sockfd, (struct sockaddr*)&client_addr, &client_addr_len);
    if (newsockfd < 0) {
        perror("Accept failed");
        close(sockfd);
        return 1;
    }

    // Generate a random number between 100 and 999
    srand(time(NULL));
    int random_number = rand() % 900 + 100;

    printf("Server generated random number: %d\n", random_number);

    // Convert the random number to a string
    snprintf(buffer, sizeof(buffer), "%d", random_number);

    // Send the random number to the client
    if (send(newsockfd, buffer, strlen(buffer), 0) < 0) {
        perror("Error sending data");
        close(newsockfd);
        close(sockfd);
        return 1;
    }

    close(newsockfd);
    close(sockfd);
    return 0;
}

