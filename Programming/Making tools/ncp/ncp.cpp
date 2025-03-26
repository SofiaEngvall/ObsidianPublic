// ncp - Simple network file copy program

// TO DO:
// Add non recursive option (or rather make it an option)
// Add list mode, to just list the files that would be sent

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
    if (argc >= 2 && (strcmp(argv[1], "send") == 0 || strcmp(argv[1], "s") == 0))
    {
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
        if (argc >= 5 && !networkFileCopy.setOriginPath(argv[4]))
        {
            std::cerr << "Incorrect file/folder path: " << argv[4] << std::endl;
            listSyntax();
            return 1;
        }
        else if (argc == 4 && !networkFileCopy.setOriginPath())
        {
            std::cerr << "The current directory is not a directory." << std::endl;
            listSyntax();
            return 1;
        }

        networkFileCopy.isSending();
        networkFileCopy.enumFiles();
        networkFileCopy.initConnection();
        if (networkFileCopy.sendFileList())
            networkFileCopy.sendFiles();
    }

    // Receive mode
    else if (argc >= 2 && (strcmp(argv[1], "receive") == 0 || strcmp(argv[1], "r") == 0))
    {
        // Get port
        if (argc >= 3 && !networkFileCopy.setPort(argv[2]))
        {
            std::cerr << "Incorrect port number." << std::endl;
            listSyntax();
            return 1;
        }
        // Check if a filename/path is provided
        if (argc >= 4 && !networkFileCopy.setDestinationPath(argv[3]))
        {
            std::cerr << "Incorrect file/folder path: " << argv[3] << std::endl;
            listSyntax();
            return 1;
        }
        else if (argc == 3 && !networkFileCopy.setDestinationPath())
        {
            std::cerr << "The current directory is not a directory." << std::endl;
            listSyntax();
            return 1;
        }

        networkFileCopy.isReceiving();
        networkFileCopy.initConnection();
        networkFileCopy.receiveFileList();
        // networkFileCopy.receiveFiles();
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
