#include <string.h>
#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <arpa/inet.h>
#include <netdb.h>

int main(int argc, char *argv[]) {
    if(argc < 3) {
        printf("Usage: %s <target> <brute_file>\n", argv[0]);
        return 1; // Exit if not enough arguments are provided
    }

    char *target = argv[1];
    FILE *brute = fopen(argv[2], "r");
    if(brute == NULL) {
        printf("File %s could not be opened.\n", argv[2]);
        return 1;
    }

    char txt[50];
    //aloca na memoria os resultados porque tive problemas de buffer  
    char result[1024]; 

    while(fscanf(brute, "%49s", txt) == 1) { 
       snprintf(result, sizeof(result), "%s%s", txt, target); // Safely format string with bounds
        struct hostent *host = gethostbyname(result);
        if(host == NULL) {
            printf("Could not resolve host: %s\n", result);
            continue;
        }
        printf("HOST FOUND: %s ====> IP: %s \n", result, inet_ntoa(*((struct in_addr *)host->h_addr)));
    }

    fclose(brute); // Close the file
    return 0;
}
