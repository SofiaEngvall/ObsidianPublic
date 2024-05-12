#include <iostream>
#include <cstring>

#include "TCPTalk.h"
#include "NetworkFileCopy.h"

void listSyntax()
{
    std::cout << "Usage: ncp send <ip> <port> [file/folder path]" << std::endl;
    std::cout << "Usage: ncp receive <port> [destination path]" << std::endl;
    std::cout << "If no file/folder path is supplied the default is the current directory." << std::endl;
}

int main(int argc, char *argv[])
{
    NetworkFileCopy networkFileCopy;

    if (argc == 2)
    {
        std::cerr << "Please set the parameters." << std::endl;
        listSyntax();
        return 1;
    }
    // Send mode
    if (argc >= 2 && strcmp(argv[1], "send") == 0)
    {
        networkFileCopy.isSending();
        // Get ip
        if (argc >= 3 && !networkFileCopy.setIP(argv[2]))
        {
            std::cerr << "Incorrect IPv4 address format." << std::endl;
            listSyntax();
            return 1;
        }
        // Get port
        if (argc >= 4 && !networkFileCopy.setPort(argv[3]))
        {
            std::cerr << "Incorrect port number." << std::endl;
            listSyntax();
            return 1;
        }
        // Check if a filename/path is provided
        if (argc >= 5 && !networkFileCopy.setPath(argv[4]))
        {
            std::cerr << "Incorrect file/folder path: " << argv[4] << std::endl;
            listSyntax();
            return 1;
        }
        else if (argc == 4 && !networkFileCopy.setPath())
        {
            std::cerr << "The current directory is not a directory." << std::endl;
            listSyntax();
            return 1;
        }

        networkFileCopy.enumFiles();
        networkFileCopy.initConnection();
        // networkFileCopy.sendFileList();
        // networkFileCopy.sendFiles();
    }

    // Receive mode
    else if (argc >= 2 && strcmp(argv[1], "receive") == 0)
    {
        networkFileCopy.isReceiving();
        // NetworkFileCopy.receiveFileList();
        // NetworkFileCopy.receiveFiles();
    }

    // Unknown mode
    else
    {
        std::cerr << "Choose send or receive." << std::endl;
        listSyntax();
        return 1;
    }
    return 0;
}
