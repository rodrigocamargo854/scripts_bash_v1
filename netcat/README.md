
#

## Características

- Escutar em uma porta específica aguardando por conexões.
- Executar um comando específico ao receber uma conexão e enviar sua saída de volta ao cliente.
- Aceitar conexões para transferir arquivos para um local específico no servidor.
- Permitir um shell interativo para execução de comandos remotos.

## Opções Disponíveis

- `-h` ou `--help`: Mostra a mensagem de ajuda.
- `-l` ou `--listen`: Ativa o modo de escuta para aceitar conexões inbound.
- `-e` ou `--execute=file_to_run`: Executa um comando específico ao receber uma conexão.
- `-c` ou `--command`: Inicializa um shell interativo para comandos remotos.
- `-u` ou `--upload=destination`: Especifica um local para salvar arquivos transferidos durante a conexão.
- `-t` ou `--target`: Define o alvo da conexão.
- `-p` ou `--port`: Especifica a porta para escutar ou conectar.

## Exemplos de Uso

### Modo Servidor (Escuta)

Para iniciar o servidor e escutar por conexões:

```sh
python bhpnet.py -l -p 5555 -c
```

Para executar um comando ao receber uma conexão:

```sh
python bhpnet.py -l -p 5555 -e="cat /etc/passwd"
```

Para receber um arquivo:

```sh
python bhpnet.py -l -p 5555 -u=/path/to/save/file
```

### Modo Cliente (Conectar)

Para enviar um comando simples:

```sh
echo 'Hello, world!' | python bhpnet.py -t host.com -p 5555
```

Para transferir um arquivo:

```sh
python bhpnet.py -t host.com -p 5555 -u=/path/on/server
```
###referência
```
retirado do livro black_hat python

```
