
#include <stdio.h>
#include <sys/socket.h>
#include <netinet/in.h> 
#include <arpa/inet.h> 
#include <unistd.h> 

int main(int argc, char *argv[]) {

    int my_socket;
    int connection;
    
    int port;
    int start=0;
    int final=65535;
    char *final_target; 
    final_target=argv[1];

    
    struct sockaddr_in target;

    for (port=start;port<final;port++){

    my_socket = socket(AF_INET, SOCK_STREAM, 0);
    target.sin_family = AF_INET;
    target.sin_port = htons(port);
    target.sin_addr.s_addr = inet_addr(final_target); 
    connection = connect(my_socket, (struct sockaddr *)&target, sizeof(target));
    
    if (connection == 0) {
        printf("Door opened %d status  \n",port);
    } else {

    close(my_socket); 
   
   }
  }  
return 0;

}

