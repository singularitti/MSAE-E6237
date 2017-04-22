#!/bin/zsh

for file in avec e eal
do
    gsed -i '1d' $file
    gsed -i 's/^ //g' $file
done
