#include <stdio.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <arpa/inet.h>
#include <unistd.h>

#define PORT 21 // Porta de FTP

int main(int argc, char *argv[]) {
    if (argc != 2) {
        printf("Usage: %s <IP address>\n", argv[0]);
        return 1;
    }

    const char *ip = argv[1];
    struct sockaddr_in target;
    int sock;
    int connectionResult;
    int attempts = 0;

    target.sin_family = AF_INET;
    target.sin_port = htons(PORT);
    inet_pton(AF_INET, ip, &target.sin_addr);

    while (1) { // Loop infinito
        sock = socket(AF_INET, SOCK_STREAM, 0);
        if (sock < 0) {
            perror("Socket creation failed");
            continue;
        }

        connectionResult = connect(sock, (struct sockaddr *)&target, sizeof(target));
        if (connectionResult == 0) {
            printf("Ping %d: Conexão estabelecida com %s na porta %d\n", ++attempts, ip, PORT);
        } else {
            perror("Conexão falhou");
        }

        close(sock);
        usleep(500000); // Espera 0.1 segundo antes da próxima tentativa
    }

    // Este ponto nunca será alcançado
    return 0;
}

