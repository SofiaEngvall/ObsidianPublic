#ifndef TCPTALK_H
#define TCPTALK_H

#include <arpa/inet.h>

class TCPTalk
{
private:
    in_addr_t ip; // Compatible with struct s_addr - A 4-byte number that represents one digit in an IP address per byte
    uint16_t port;
    int tcpSocket;             // Socket address
    int connectedSocket;       // Socket connected to after listening
    sockaddr_in socketAddress; // Struct for connection data for binding the main socket

public:
    TCPTalk(const uint16_t &port);
    TCPTalk(const in_addr_t &ip, const uint16_t &port);
    ~TCPTalk();

    bool initTCPSocket();
    bool listenForConnaction();
    bool waitForAndAcceptConnection();
    void receiveData();
    void closeSocket();
    void makeConnection();
    void sendData(const char *message);
};

#endif
