#include <sys/socket.h>
#include <netdb.h>
#include <stdio.h>
#include <stdlib.h>
#include <netinet/in.h> 
#include <arpa/inet.h> 
#include <unistd.h> 

int main(int argc, char *argv[] ){
	if(argc !=2){
		printf("USO:%s <IP>\n",argv[0]);
		return 1;
	}


	int my_socket;
	int connection;
	
   	struct sockaddr_in target;
	
	my_socket= socket(AF_INET,SOCK_STREAM,0);
	target.sin_family=AF_INET;
	target.sin_port=htons(80);
	target.sin_addr.s_addr=inet_addr(argv[1]);

	connection=connect(my_socket,(struct sockaddr *)&target,sizeof target);
	
	if(connection==0){
		printf("door opened \n");
	} else {
		printf("Closed door \n");

	}

close(my_socket); 
    return 0;

}

