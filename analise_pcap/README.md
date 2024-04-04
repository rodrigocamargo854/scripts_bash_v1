
# Analise PCAP

Este script analisa arquivos PCAP para detectar possíveis comportamentos de malware, listando conexões suspeitas, subdomínios relacionados e informações sobre portas abertas. Além disso, faz uso da API do VirusTotal para enriquecer a análise com dados externos.

## Pré-requisitos

- Linux ou um ambiente Unix-like
- tcpdump instalado no sistema
- jq instalado no sistema (para processar JSON)
- curl ou wget (para requisições HTTP)
- Uma conta no VirusTotal para obter uma chave de API

## Configuração

1. **Instalar dependências:**

Garanta que `tcpdump`, `jq`, `curl` (ou `wget`) estejam instalados no seu sistema. Em sistemas baseados em Debian (como Ubuntu), você pode instalar esses pacotes usando:

```bash
sudo apt-get update
sudo apt-get install tcpdump jq curl
```

2. **Obter a chave da API do VirusTotal:**

Para utilizar a funcionalidade completa do script, é necessário obter uma chave da API do VirusTotal. Siga estes passos para obtê-la:

- Crie uma conta no [VirusTotal](https://www.virustotal.com/gui/home/upload).
- Navegue até a seção de API na sua conta do VirusTotal para gerar sua chave de API.
- Substitua o valor de `API_KEY` no script com sua chave de API pessoal.

## Uso

Para utilizar o script, simplesmente execute-o passando um arquivo PCAP como argumento:

```bash
./analise_pcap.sh arquivo.pcap
```

O script verificará se o `tcpdump` está instalado, instalará se necessário, e então procederá com a análise do arquivo PCAP fornecido.

## Contribuindo

Sinta-se à vontade para contribuir com melhorias no script. Pull requests são bem-vindos. Para grandes mudanças, por favor, abra uma issue primeiro para discutir o que você gostaria de mudar.

## Licença

[MIT](https://choosealicense.com/licenses/mit/)
