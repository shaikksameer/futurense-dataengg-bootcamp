#!/bin/bash
# Counting the number of lines in a list of files 
# for loop over arguments

if [ $# -lt 1]
then
    echo "Usage: $0 file ..."
    exit 1

fi

line_counts()
{
    f=$1
    l=`wc -l $f`
    return $l
}
echo "$0 counts the lines of code "
l=0
for f in $*
do
    echo "$f"
    # l= `wc -l $f`
    line_counts $f
    lc=$?
    echo $lc
    # n=$[ $n + 1]
    # s=$[ $s + $1 ]
done