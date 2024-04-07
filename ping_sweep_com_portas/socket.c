#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <arpa/inet.h> 
#include <unistd.h> 

#define MAX_IP_LENGTH 16 

int main(int argc, char *argv[]) {
    if (argc != 2) {
        printf("Uso: %s <arquivo_com_ips.txt>\n", argv[0]);
        return 1; 
    }

    FILE *file = fopen(argv[1], "r");
    
	if (file == NULL) {
        perror("Erro ao abrir o arquivo");
        return 2;
    }

    char ip[MAX_IP_LENGTH];
    while (fgets(ip, MAX_IP_LENGTH, file) != NULL) {
        
        ip[strcspn(ip, "\n")] = 0;

        int my_socket = socket(AF_INET, SOCK_STREAM, 0);
        struct sockaddr_in target;

        target.sin_family = AF_INET;
        target.sin_port = htons(80);
        target.sin_addr.s_addr = inet_addr(ip);

        int connection = connect(my_socket, (struct sockaddr *)&target, sizeof(target));

        if (connection == 0) {
            printf("Porta aberta em %s\n", ip);
        } else {
            printf("Porta fechada em %s\n", ip);
        }

        close(my_socket);
    }

    fclose(file);
    return 0;
}

