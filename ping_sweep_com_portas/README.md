# Varredura de Hosts e Portas

Este script realiza uma varredura (ping sweep) em uma sub-rede específica para identificar hosts ativos. Para cada host ativo encontrado, ele também verifica a abertura de portas específicas. Utiliza `hping3` para enviar pacotes SYN e aguarda respostas SYN-ACK, indicando que a porta está aberta.

## Pré-requisitos

- `hping3` instalado no seu sistema. `hping3` é uma ferramenta de análise de rede que pode enviar pacotes TCP, UDP ou ICMP customizados e exibir respostas do alvo.
  
  Para instalar `hping3` em sistemas baseados em Debian/Ubuntu:
  ```bash
  sudo apt-get update
  sudo apt-get install hping3
