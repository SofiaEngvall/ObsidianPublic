#include <iostream>
#include <filesystem>
#include <regex>

#include "NetworkFileCopy.h"

NetworkFileCopy::NetworkFileCopy()
{
    isSendMode = false;
    ip = INADDR_NONE;
    port = -1;
    path = "";
    tcpTalk = nullptr;
}

NetworkFileCopy::~NetworkFileCopy()
{
    if (tcpTalk != nullptr)
    {
        delete tcpTalk;
        tcpTalk = nullptr;
    }
}

void NetworkFileCopy::isSending()
{
    this->isSendMode = true;
}
void NetworkFileCopy::isReceiving()
{
    this->isSendMode = false;
}

bool NetworkFileCopy::setIP(const char *ip)
{ // Add IPv6
    if (std::regex_match(ip, std::regex("^((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])$")))
    {
        this->ip = inet_addr(ip); // or inet_pton if adding ipv6?
        if (this->ip == INADDR_NONE)
            return false;
        return true;
    }
    else
    {
        return false;
    }
}

bool NetworkFileCopy::setPort(const std::string &port)
{
    if (std::regex_match(port, std::regex("^(6553[0-5])|(655[0-2][0-9])|(65[0-4][0-9]{2})|(6[0-4][0-9]{3})|([0-5]?[0-9]{0,3}[0-9])")))
    {
        try
        {
            this->port = std::stoi(port);
            return true;
        }
        catch (const std::invalid_argument &e)
        {
            std::cerr << "Invalid port number: " << e.what() << std::endl;
            return false;
        }
        catch (const std::out_of_range &e)
        {
            std::cerr << "Port number out of range: " << e.what() << std::endl;
            return false;
        }
    }
    else
    {
        return false;
    }
}

bool NetworkFileCopy::setPath()
{
    if (std::filesystem::is_directory(std::filesystem::current_path()))
    {
        this->path = std::filesystem::current_path();
        std::cout << "No file/path input provided, using current directory: " << this->path << std::endl;
        return true;
    }
    return false;
}
bool NetworkFileCopy::setPath(const std::string &path)
{
    // File
    if (std::filesystem::is_regular_file(path))
    {
        this->path = path;
        std::cout << "File name supplied: " << this->path << std::endl;
        return true;
    }
    // Directory
    else if (std::filesystem::is_directory(path))
    {
        this->path = path;
        std::cout << "Directory name supplied: " << this->path << std::endl;
        return true;
    }
    return false;
}

void NetworkFileCopy::enumFiles()
{ // Add non recursive option
    std::cout << "Generating file list..." << std::endl
              << std::endl;
    std::cout << "  Filesize  Filename                        Filepath" << std::endl;
    // std::cout << "Filename        Filepath                  Filesize" << std::endl;
    std::cout << "--------------------------------------------------------------------------------" << std::endl;
    if (std::filesystem::is_directory(path))
    {
        // Add non recursive version
        for (const auto &entry : std::filesystem::recursive_directory_iterator(path))
        {
            if (std::filesystem::is_regular_file(entry))
            {
                FileItem file;
                file.filename = entry.path().filename().string();
                file.filepath = entry.path().string();
                file.filesize = std::filesystem::file_size(entry);
                fileList.push_back(file);
                std::cout << std::setw(10) << std::right << file.filesize << "  "
                          << std::setw(30) << std::left << file.filename << "  "
                          << std::setw(25) << std::left << file.filepath << std::endl;
            }
        }
    }
    // Path is a filemane
    else
    {
        std::filesystem::path pathObj(path);
        FileItem file;
        file.filename = pathObj.filename().string();
        file.filepath = pathObj.string();
        file.filesize = std::filesystem::file_size(pathObj);
        fileList.push_back(file);
        std::cout << std::setw(16) << std::left << file.filename << " " << std::setw(25) << std::left << file.filepath << " " << file.filesize << std::endl;
    }
}

bool NetworkFileCopy::initConnection()
{
    if (isSendMode)
    {
        if (tcpTalk == nullptr)
        {
            tcpTalk = new TCPTalk(ip, port);
        }
    }
    else
    { // Receiving Listening on all ports
        if (tcpTalk == nullptr)
        {
            tcpTalk = new TCPTalk(port);
        }
    }
    if (!tcpTalk->initTCPSocket())
    {
        return false;
    }
    return true;
}

void NetworkFileCopy::sendFileList()
{
}

void NetworkFileCopy::receiveFileList()
{
}

void NetworkFileCopy::sendFiles()
{
}

void NetworkFileCopy::receiveFiles()
{
}
