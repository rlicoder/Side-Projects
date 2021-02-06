#include <stdio.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <unistd.h>
#include <iostream>
#include <string.h>
#include <string>

using namespace std;

void handle(int socket);
void errMsg(const string &s);

int main(int argc, char** argv) {
    //Declare variables
    int serverSocket, clientSocket, portNum, msgSize, pid;
    socklen_t clientLen;
    char msg[256];
    struct sockaddr_in serverAddress, clientAddress;
    
    //If port number provided through command line argument is invalid
    if(argc < 2) errMsg("INVALID PORT NUMBER\n");
    
    //Create the socket for the server
    serverSocket = socket(AF_INET, SOCK_STREAM, 0);//Over internet, stream type socket, and auto choose protocol
    
    //If socket failed to open
    if(serverSocket < 0) errMsg("SOCKET FAILED TO OPEN\n");
    
    //Set each byte of server address to 0
    memset((char *) &serverAddress, 0, sizeof(serverAddress));
    
    //Get port number from command line argument
    portNum = atoi(argv[1]);
    
    //Set values for server address
    serverAddress.sin_family = AF_INET;//Same as socket address domain, over internet
    serverAddress.sin_port = htons(portNum);//Set port number on server address after converting to network byte order from host byte order
    serverAddress.sin_addr.s_addr = INADDR_ANY;//Set ip address for server, gets ip of local machine
    
    //Attempt to bind the server socket to the server address
    if(bind(serverSocket, (struct sockaddr *) &serverAddress, sizeof(serverAddress)) < 0) //If failed to bind
        errMsg("FAILED TO BIND SERVER SOCKET TO SERVER ADDRESS\n");
    
    //Listen on server socket with queue size up to 5
    listen(serverSocket, 5);
    
    //Get length of client address
    clientLen = sizeof(clientAddress);
    
    //Loop indefinitely
    while(true) {
        //Accept connection from client socket
        clientSocket = accept(serverSocket, (struct sockaddr *) &clientAddress, &clientLen);//Pass in listening socket, address of client, and size of client address length

        //If failed to accept connection from the client address
        if(clientSocket < 0) errMsg("FAILURE TO CONNECT TO THE CLIENT ADDRESS\n");
        
        //Create fork to handle connection
        pid = fork();
        
        //Check if failed to fork
        if(pid < 0) errMsg("FAILED TO FORK\n");
        
        if(pid == 0) {
            close(serverSocket);
            handle(clientSocket);
            exit(0);
        }
        else {
            close(clientSocket);
        }
    }
    close(serverSocket);
    
    return 0;
}

void handle(int clientSocket) {
    //Declare and intialize variables
    int msgSize;
    char msg[256];
    memset(msg, 0, sizeof(msg));
    
    //Read message
    msgSize = read(clientSocket, msg, 255);
    
    //If failed to read message
    if(msgSize < 0) errMsg("FAILED TO READ MESSAGE FROM CLIENT\n");
    
    //Print message
    fputs(msg, stdout);
}

void errMsg(const string &s) {
    fputs(s.c_str(), stdout);
    exit(EXIT_FAILURE);
}
