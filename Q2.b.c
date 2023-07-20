// Ahmad Haziq Khalis bin Khairul Anuar 2021619528
// Question 2 - Write a client program to retrieve random number from server and display it accordingly

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <arpa/inet.h>

#define SERVER_PORT 8080
#define MAX_BUFFER_SIZE 4 // Buffer size to receive the random number 

int main() {
    int sockfd;
    struct sockaddr_in server_addr;
    char buffer[MAX_BUFFER_SIZE];
    char server_ip[16]; // Buffer to store the server IP address (IPv4)

    printf("Enter the server IP address: ");
    if (fgets(server_ip, sizeof(server_ip), stdin) == NULL) {
        perror("Error reading server IP address");
        return 1;
    }

    // Remove trailing newline from the server IP
    server_ip[strcspn(server_ip, "\n")] = '\0';

    // Create a TCP socket
    sockfd = socket(AF_INET, SOCK_STREAM, 0);
    if (sockfd < 0) {
        perror("Error creating socket");
        return 1;
    }

    // Configure server address
    memset(&server_addr, 0, sizeof(server_addr));
    server_addr.sin_family = AF_INET;
    server_addr.sin_port = htons(SERVER_PORT);
    if (inet_pton(AF_INET, server_ip, &server_addr.sin_addr) <= 0) {
        perror("Invalid server IP address");
        close(sockfd);
        return 1;
    }

    // Connect to the server
    if (connect(sockfd, (struct sockaddr*)&server_addr, sizeof(server_addr)) < 0) {
        perror("Connection failed");
        close(sockfd);
        return 1;
    }

    // Receive the random number from the server
    int bytes_received = recv(sockfd, buffer, MAX_BUFFER_SIZE - 1, 0);
    if (bytes_received < 0) {
        perror("Error receiving data");
        close(sockfd);
        return 1;
    }

    // Null-terminate the received data
    buffer[bytes_received] = '\0';

    // Convert the received string back to an integer
    int random_number = atoi(buffer);

    printf("Received random number from server: %d\n", random_number);

    close(sockfd);
    return 0;
}



