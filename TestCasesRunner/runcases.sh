#!bin/bash

run=*.cpp
g++ $run

cd /cases
for file in *.in;
do
    ./a.out < $file > o.txt
    filename="${file%.*}"
    echo $filename
    diff $filename.ans o.txt
done

