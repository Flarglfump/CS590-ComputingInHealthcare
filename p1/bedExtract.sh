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

if [ ! -d "$DATADIR/pos/txt" ]; then
    mkdir "$DATADIR/pos/txt"
fi
if [ ! -d "$DATADIR/neg/txt" ]; then
    mkdir "$DATADIR/neg/txt"
fi

for FILE in $DATADIR/pos/*.bed; do
    FILEBASENAME=$(basename -- "$FILE")
    FILEBASENAME="${FILEBASENAME%.*}"
    echo bedtools getfasta -fi "$REF_GENOME" -bed "$FILE" -fo "$DATADIR/pos/txt/$FILEBASENAME.txt"
    bedtools getfasta -fi "$REF_GENOME" -bed "$FILE" -fo "$DATADIR/pos/txt/$FILEBASENAME.txt"
done

for FILE in $DATADIR/neg/*.bed; do
    FILEBASENAME=$(basename -- "$FILE")
    FILEBASENAME="${FILEBASENAME%.*}"
    echo bedtools getfasta -fi "$REF_GENOME" -bed "$FILE" -fo "$DATADIR/neg/txt/$FILEBASENAME.txt"
    bedtools getfasta -fi "$REF_GENOME" -bed "$FILE" -fo "$DATADIR/neg/txt/$FILEBASENAME.txt"
done
