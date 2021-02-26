#!bin/bash

for i in {1..10000}:
do
    python3 submit.py
    echo $i
done
