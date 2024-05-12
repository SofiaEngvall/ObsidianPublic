#include <cstring>
#include <iostream>
#include <regex>

#include "NetworkFileCopy.h"

NetworkFileCopy::NetworkFileCopy() : tcpTalk()
{
    isSendMode = false;
    ip = INADDR_NONE;
    port = -1;
    path = "";
    destPath = "";
}

NetworkFileCopy::~NetworkFileCopy()
{
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

bool NetworkFileCopy::setPath(std::filesystem::path &path)
{
    if (std::filesystem::is_directory(std::filesystem::current_path()))
    {
        path = std::filesystem::current_path();
        std::cout << "No file/path input provided, using current directory: " << path << std::endl;
        return true;
    }
    return false;
}
bool NetworkFileCopy::setPath(std::filesystem::path &path, const std::filesystem::path &inPath)
{
    if (std::filesystem::is_regular_file(inPath) || std::filesystem::is_directory(inPath))
    {
        path = inPath;
        std::cout << "Path supplied: " << path << std::endl;
        return true;
    }
    return false;
}

bool NetworkFileCopy::setOriginPath()
{
    return setPath(this->path);
}
bool NetworkFileCopy::setOriginPath(const std::filesystem::path &path)
{
    return setPath(this->path, path);
}

bool NetworkFileCopy::setDestinationPath()
{
    return setPath(this->destPath);
}
bool NetworkFileCopy::setDestinationPath(const std::filesystem::path &path)
{
    return setPath(this->destPath, path);
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
        tcpTalk.initSender(ip, port);
    else // Receiving = Listening on all ports
        tcpTalk.initReceiver(port);

    if (!tcpTalk.initTCPSocket())
        return false;

    if (isSendMode)
        tcpTalk.makeConnection();
    else // Receiving
        tcpTalk.listenForConnection();

    return true;
}

bool NetworkFileCopy::sendFileList()
{
    // Calculate data size
    std::vector<FileItem>::size_type dataSize = 0;
    for (const FileItem &file : fileList)
    {
        dataSize += file.filename.string().size() + 1; // +1 for null terminator
        dataSize += file.filepath.string().size() + 1; // +1 for null terminator
        dataSize += sizeof(uint64_t);                  // Size of the filesize field
    }

    // Allocate memory
    char *serializedFileList = new char[dataSize];
    char *currentPos = serializedFileList;

    // Serialize each file item
    for (const FileItem &file : fileList)
    {
        std::strcpy(currentPos, file.filename.c_str());
        currentPos += file.filename.string().size() + 1;

        std::strcpy(currentPos, file.filepath.c_str());
        currentPos += file.filepath.string().size() + 1;

        std::memcpy(currentPos, &file.filesize, sizeof(uint64_t));
        currentPos += sizeof(uint64_t);
    }

    // Send data
    if (!tcpTalk.sendData(serializedFileList))
    {
        delete[] serializedFileList;
        return false;
    }

    delete[] serializedFileList;
    return true;
}

/*
        //serializedFileList = fileList somehow;
        for(FileItem &file: fileList){
            std::cout << file.filename << std::endl;
            std::cout << file.filepath << std::endl;
            std::cout << file.filesize << std::endl;
        }

        //if(!tcpTalk.sendData(serializedFileList))
        if(!tcpTalk.sendData("test"))
            return false;


        return true;
    }
*/
void NetworkFileCopy::receiveFileList()
{
    std::cout << "Reveived data: " << tcpTalk.receiveData() << std::endl;
}

void NetworkFileCopy::sendFiles()
{
    // add checksum
}

void NetworkFileCopy::receiveFiles()
{
    // check checksum
}
