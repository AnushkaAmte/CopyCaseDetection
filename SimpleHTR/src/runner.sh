#!/bin/bash
for ((i=0; i<=4; i++))
do
for((j=0;j<=4;j++))
do
    python3 main.py --img_file ../data/detected/$i$j.png
    sleep 1
done
done

