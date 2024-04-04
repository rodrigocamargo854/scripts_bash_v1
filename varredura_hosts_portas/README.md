# Varredura de Hosts e Portas com `varredura_hosts_portas.sh`

Este script realiza uma varredura em uma sub-rede especificada para identificar hosts ativos e verifica se determinadas portas estão abertas nesses hosts. É uma ferramenta útil para administradores de rede e profissionais de segurança para realizar uma rápida checagem de segurança da rede.

## Pré-requisitos

- `hping3` deve estar instalado no sistema. `hping3` é uma ferramenta avançada de teste de rede que envia pacotes TCP/IP customizados e analisa as respostas.
  
  Para instalar `hping3` em sistemas Debian/Ubuntu:
  ```bash
  sudo apt-get update
  sudo apt-get install hping3
