#include <stdio.h>
#include <netdb.h>
#include <arpa/inet.h>

int main(int argc, char *argv[]){
    if(argc <= 1){
        printf("Modo de uso: ./get_host_by_name <host>\n");
        return 1; 
    } else {
        struct hostent *alvo = gethostbyname(argv[1]);
        if(alvo == NULL){
            printf("Ocorreu um erro.\n");
            return 1;
        } else {
           
            printf("IP: %s\n", inet_ntoa(*((struct in_addr *)alvo->h_addr)));
        }
    }
    return 0; 
}
