#/usr/bin/bash

DATADIR="/users/gwitske/CS590-ComputingInHealthcare/p1/data" 
REF_GENOME="/users/gwitske/CS590-ComputingInHealthcare/p1/reference/hg38.fa"

if [ ! -d "$DATADIR" ]; then
    echo "$DATADIR does not exist!"
    exit
fi

if [ ! -f "$REF_GENOME" ]; then
    echo "$$REF_GENOME does not exist!"
    exit
fi

if [ ! -d "$DATADIR/txt" ]; then
    mkdir "$DATADIR/txt"
fi

for FILE in $DATADIR/*.bed; do
    FILEBASENAME=$(basename -- "$FILE")
    FILEBASENAME="${FILEBASENAME%.*}"
    echo bedtools getfasta -fi "$REF_GENOME" -bed "$FILE" -fo "$DATADIR/txt/$FILEBASENAME.txt"
    bedtools getfasta -fi "$REF_GENOME" -bed "$FILE" -fo "$DATADIR/txt/$FILEBASENAME.txt"

done
