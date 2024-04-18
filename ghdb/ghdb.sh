#!/bin/bash

TARGET=$1
SEARCH="curl"

echo "pastebin searching"
$SEARCH 'https://google.com/search?q=site:pastebin.com+$TARGET' 2> /dev/null
echo "Trello searching"
$SEARCH 'https://google.com/search?q=site:trello.com+$TARGET'   2> /dev/null 
echo "searching web"
$SEARCH 'https://google.com/search?q=$TARGET+ext:php+OR+ext:asp' 2> /dev/null 
