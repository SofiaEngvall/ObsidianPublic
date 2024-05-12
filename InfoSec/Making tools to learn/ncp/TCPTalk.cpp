#include <cstring>
#include <iostream>
#include <string>

#include <netinet/in.h>
#include <sys/socket.h>
#include <unistd.h>

#include "TCPTalk.h"

// TCPTalk::~TCPTalk(){
//     this->ip = INADDR_ANY; // Listen on all IPs, value is zero
//     this->port = -1;
//     int tcpSocket = -1;
//     int connectedSocket = -1;
// }

TCPTalk::TCPTalk(const uint16_t &port)
{
    this->ip = INADDR_ANY; // Listen on all IPs, value is zero
    this->port = port;
    int tcpSocket = -1;
    int connectedSocket = -1;
}
TCPTalk::TCPTalk(const in_addr_t &ip, const uint16_t &port)
{
    this->ip = ip;
    this->port = port;
    int tcpSocket = -1;
    int connectedSocket = -1;
}

TCPTalk::~TCPTalk()
{
}

bool TCPTalk::initTCPSocket()
{
    if ((tcpSocket = socket(AF_INET, SOCK_STREAM, 0)) < 0)
    { // IPv4 TCP IP socket
        std::cerr << "Error creating socket." << std::endl;
        return false;
    }

    socketAddress.sin_family = AF_INET;   // IPv4
    socketAddress.sin_port = htons(port); // Converts to network byte order
    socketAddress.sin_addr.s_addr = ip;

    // Bind the socket to the ip and port specified in socketAdress
    if (bind(tcpSocket, (struct sockaddr *)&socketAddress, sizeof(socketAddress)) < 0)
    {
        std::cerr << "Error connecting socket to IP and port." << std::endl;
        return false;
    }
    return true;
}

bool TCPTalk::listenForConnaction()
{
    if (listen(tcpSocket, 1) < 0)
    { // Max 1 connection in queue, only one connection expected
        std::cerr << "Failed to listen on socket." << std::endl;
        return false;
    }
    return true;
}

bool TCPTalk::waitForAndAcceptConnection()
{
    // Blocks program until connection is received
    if ((connectedSocket = accept(tcpSocket, nullptr, nullptr)))
    { // connect after listening
        std::cerr << "Failed to connect to sender." << std::endl;
        return false;
    }
    return true;
}

void TCPTalk::receiveData()
{
    char buffer[1024];
    int recvBytes = 0;
    while (true)
    {
        memset(buffer, 0, 1024); // clear buffer
    }
    if (((recvBytes = recv(connectedSocket, buffer, sizeof(buffer), 0)) < 0))
    {
        std::cerr << "Connection issues." << std::endl;
    }
    if (recvBytes == 0)
    {
        std::cerr << "Sender disconnected/File done." << std::endl;
    }

    std::cout << "Reveived data: " << std::string(buffer, 0, recvBytes) << std::endl;
}

void TCPTalk::closeSocket()
{
    close(tcpSocket);
}

void TCPTalk::makeConnection()
{
    if ((connect(tcpSocket, (struct sockaddr *)&socketAddress, sizeof(socketAddress))) < 0)
    {
        std::cerr << "Error making connection." << std::endl;
    }
}

void TCPTalk::sendData(const char *message)
{
    send(tcpSocket, message, strlen(message), 0);
}
