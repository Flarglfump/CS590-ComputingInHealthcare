#/usr/bin/bash

DATADIR="data" 
REF_GENOME="reference/hg38.fa"

if [ ! -d "$DATADIR" ]; then
    echo "$DATADIR does not exist!"
    exit
fi

if [ ! -f "$REF_GENOME" ]; then
    echo "$$REF_GENOME does not exist!"
    exit
fi

if [ ! -d "$DATADIR/pos" ]; then
    mkdir "$DATADIR/pos"
fi
if [ ! -d "$DATADIR/neg" ]; then
    mkdir "$DATADIR/neg"
fi

# Positive Files
for FILE in $DATADIR/pos/*.bed; do
    FILEBASENAME=$(basename -- "$FILE")
    echo "Processing file \"$FILEBASENAME\""
    FILEBASENAME="${FILEBASENAME%.*}"
    bedtools getfasta -fi "$REF_GENOME" -bed "$FILE" -fo "$DATADIR/pos/$FILEBASENAME.txt" && rm "$FILE"
done

# Negative Files
for FILE in $DATADIR/neg/*.bed; do
    FILEBASENAME=$(basename -- "$FILE")
    echo "Processing file \"$FILEBASENAME\""
    FILEBASENAME="${FILEBASENAME%.*}"
    bedtools getfasta -fi "$REF_GENOME" -bed "$FILE" -fo "$DATADIR/neg/$FILEBASENAME.txt" && rm "$FILE"
done
