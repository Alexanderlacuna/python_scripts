#!/bin/bash
i=1
for package in $(cat warning.txt | grep "dpkg: warning: files list file for package " | grep -Po "'[^']*'" | sed "s/'//g")；
do
  echo "No.${i} ==================start intall ${package}==================="
  apt-get install --reinstall "$package" -y;
  #If aptitude is not installed, apt-get --reinstall "$package" can be used.
  i=`expr $i + 1`
done