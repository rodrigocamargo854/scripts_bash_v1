# README para Script de Banner Grabbing

## Descrição

Este script Python é utilizado para realizar o *banner grabbing* de diversos serviços de rede, conectando-se a portas específicas de hosts fornecidos e capturando as mensagens de boas-vindas (banners) enviadas por esses serviços. É útil para fins de reconhecimento em testes de penetração ou auditorias de segurança, permitindo identificar serviços e suas versões em execução nos hosts alvo.

## Requisitos

- Python 3.x

## Uso

```bash
python banner_grabbing.py 'host1:porta1,host2:porta2,...'
```

Substitua `host1:porta1,host2:porta2,...` pela lista de hosts e portas que você deseja escanear, separados por vírgulas.

## Como Funciona

1. O script aceita uma string contendo pares de host e porta, separados por vírgulas, como argumento da linha de comando.
2. Para cada par host:porta, o script tenta estabelecer uma conexão TCP.
3. Se a conexão for bem-sucedida, o script tenta ler o banner enviado pelo serviço na porta especificada.
4. Os banners capturados (ou mensagens de erro, se a conexão falhar) são impressos na saída padrão.

## Exemplo

```bash
python banner_grabbing.py 'www.example.com:80,192.168.1.1:22'
```

## Nota

Este script é destinado apenas para fins educacionais e de testes de segurança com permissão. Use-o de forma responsável.