#!/bin/bash

HOST=$1
TYPE=$2  

lynx -dump "http://google.com/search?num=500&q=site:"${HOST}"+ext:"${TYPE}"" | cut -d "=" -f2 | grep ${.TYPE} 

