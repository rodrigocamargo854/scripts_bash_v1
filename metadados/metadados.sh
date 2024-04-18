#!/bin/bash

#emails_file="todos_emails.txt"

lynx --dump "https://google.com/search?q=site:businesscorp.com.br" | grep -v "email" | grep "https" > collection.txt

# Inicializa um contador para usar nos nomes dos arquivos de saída.
counter=1

for url in $(cat collection.txt); do
    # Baixa o conteúdo da URL e procura por emails, salvando em um arquivo nomeado com o contador.
    wget -q -O - "$url" | grep -oP '[\w\.-]+@[\w\.-]+\.\w+' > "emails_$counter.txt"
    # Incrementa o contador para o próximo arquivo.
    ((counter++))
done


