#ifndef TCPTALK_H
#define TCPTALK_H

#include <string>
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
    TCPTalk();
    ~TCPTalk();

    void initReceiver(const uint16_t &port);
    void initSender(const in_addr_t &ip, const uint16_t &port);
    bool initTCPSocket();
    bool makeConnection();
    bool listenForConnection();
    bool sendData(const char *message);
    std::string receiveData();
    void closeSockets();
};

#endif
