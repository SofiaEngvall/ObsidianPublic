#include <cstring>
#include <iostream>

#include <netinet/in.h>
#include <sys/socket.h>
#include <unistd.h>
#include <arpa/inet.h>

#include "TCPTalk.h"

TCPTalk::TCPTalk()
{
    this->ip = INADDR_ANY; // Listen on all IPs, value is zero
    this->port = -1;
    tcpSocket = -1;
    connectedSocket = -1;
}

TCPTalk::~TCPTalk()
{
    closeSockets();
}

void TCPTalk::initSender(const in_addr_t &ip, const uint16_t &port)
{
    this->ip = ip;
    this->port = port;
}

void TCPTalk::initReceiver(const uint16_t &port)
{
    this->ip = INADDR_ANY; // Listen on all IPs, value is zero
    this->port = port;
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

    return true;
}

bool TCPTalk::makeConnection()
{ // Sender
    if ((connect(tcpSocket, (struct sockaddr *)&socketAddress, sizeof(socketAddress))) < 0)
    {
        std::cerr << "Connection failed. Is " << inet_ntoa(*(struct in_addr *)&ip) << " is listening on port " << port << "." << std::endl;
        return false;
    }
    return true;
}

bool TCPTalk::listenForConnection()
{ // Receiver
    // Bind the socket to the ip and port specified in socketAdress
    if (bind(tcpSocket, (struct sockaddr *)&socketAddress, sizeof(socketAddress)) < 0)
    {
        std::cerr << "Error connecting socket to IP and port." << std::endl;
        return false;
    }

    if (listen(tcpSocket, 1) < 0)
    { // Max 1 connection in queue, only one connection expected
        std::cerr << "Failed to listen on socket." << std::endl;
        return false;
    }

    // Blocks program until connection is received!
    if ((connectedSocket = accept(tcpSocket, nullptr, nullptr)) < 0)
    { // connect after listening
        std::cerr << "Failed to connect to sender." << std::endl;
        return false;
    }
    return true;
}

bool TCPTalk::sendData(const char *message)
{
    if (send(tcpSocket, message, strlen(message), 0) < 0)
        return false;
    return true;
}

std::string TCPTalk::receiveData()
{
    char buffer[1024];
    int recvBytes = 0;
    std::string received = "";
    while (true)
    {
        memset(buffer, 0, 1024); // clear buffer

        if (((recvBytes = recv(connectedSocket, buffer, sizeof(buffer), 0)) < 0))
        {
            std::cerr << "Connection issues." << std::endl;
            return "";
        }

        if (recvBytes == 0)
        {
            std::cerr << "Sender disconnected/File done." << std::endl;
            break;
        }

        received += std::string(buffer, 0, recvBytes);
    }

    std::cout << "Full data: " << received << std::endl;
    return received;
}

void TCPTalk::closeSockets()
{
    if (tcpSocket != -1)
        close(tcpSocket);
    if (connectedSocket != -1)
        close(connectedSocket);
}
