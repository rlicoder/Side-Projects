#!bin/bash

run=*.cpp
g++ $run

for file in cases/*.in;
do
    ./a.out < $file > o.txt
    filename="${file%.*}"
    echo $filename
    diff $filename.ans o.txt
done

