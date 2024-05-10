#!/bin/bash

#emails_file="todos_emails.txt"

HOST=$1

lynx --dump "https://google.com/search?q=site:$1" | grep -v "email" | grep "https" > collection.txt


counter=1

for url in $(cat collection.txt); do
    
    wget -q -O - --user-agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36" "$url" | grep -oP '[\w\.-]+@[\w\.-]+\.\w+' > "emails_$counter.txt"

    #wget -q -O - "$url" | grep -oP '[\w\.-]+@[\w\.-]+\.\w+' > "emails_$counter.txt"
    
     echo "searching..."
     ((counter++))
     sleep 10
done


