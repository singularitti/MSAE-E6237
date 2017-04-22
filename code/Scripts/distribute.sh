#!/bin/zsh
file=celq

for folder in `ls -d -- */`
do
  cp $file $folder
done
