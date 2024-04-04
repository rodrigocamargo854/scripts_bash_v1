
# Bash Security Toolkit

Bem-vindo ao Bash Security Toolkit, uma coleção de scripts em Bash para facilitar a realização de tarefas de segurança e análise de redes. Estes scripts são projetados para serem simples, porém poderosos, fornecendo funcionalidades como varredura de rede, análise de arquivos PCAP para detecção de malware, e muito mais.

## Scripts Inclusos

- `analise_pcap.sh`: Analisa arquivos PCAP para detectar comportamentos suspeitos e possíveis malwares.
- `verifica_malware_pcap.sh`: Utiliza dados de arquivos PCAP para verificar a presença de malware com base nas conexões de rede.
- `ping_sweep_com_portas.sh`: Realiza uma varredura na rede para identificar hosts ativos e verificar portas específicas.
- `varredura_hosts_portas.sh`: Similar ao script anterior, mas com foco em verificar múltiplas portas para cada host detectado.

## Pré-requisitos

Para utilizar os scripts deste repositório, você precisará de um ambiente Linux ou Unix-like com as seguintes dependências instaladas:

- tcpdump
- jq
- curl ou wget
- hping3

## Instalação

Clone este repositório em sua máquina local usando:

```bash
git clone https://github.com/seu-usuario/Bash-Security-Toolkit.git
```

Antes de executar qualquer script, assegure-se de torná-los executáveis:

```bash
chmod +x *.sh
```

## Uso

Cada script tem seu próprio conjunto de instruções e parâmetros. Para mais informações, consulte o README específico de cada script no diretório correspondente ou execute o script sem parâmetros para ver uma mensagem de ajuda.

## Contribuição

Contribuições são bem-vindas! Se você tem ideias para novos scripts ou melhorias nos existentes, sinta-se à vontade para criar um fork do repositório, fazer suas alterações, e enviar um pull request.

## Licença

Este repositório é distribuído sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.
