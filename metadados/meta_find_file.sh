#!/bin/bash
set -x

HOST=$1
TYPE=$2  

#lynx --dump "https://google.com/search?q=site:${HOST}+filetype:${TYPE}" > collection_file.txt

curl -A "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36" \
-H "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9" \
-H "Accept-Language: en-US,en;q=0.9" \
-H "Accept-Encoding: gzip, deflate, br" \
-H "Connection: keep-alive" \
"https://google.com/search?q=site:${HOST}+filetype:${TYPE}" > response.html

counter=1
grep -oP "http[^ ]+\.$TYPE\b" collection_file.txt | while IFS= read -r url; do
    echo "URL fetched: $url"  
    if curl -O "${url}"; then
        echo "File successfully downloaded: ${url}"
    else
        echo "Failed to download: ${url}"
    fi
    echo "searching..."
    ((counter++))
    sleep 10
done

