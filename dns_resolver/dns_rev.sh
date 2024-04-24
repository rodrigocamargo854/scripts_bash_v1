#!/bin/bash

IP=$1
RANGE_START=$2
RANGE_FINISH=$3

for item in $(seq $RANGE_START $RANGE_FINISH);do
host -t ptr $IP.$item;
done
