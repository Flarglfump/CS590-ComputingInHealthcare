DATADIR="data/pos" 

if [ ! -d "$DATADIR" ]; then
    echo "$DATADIR does not exist!"
    exit
fi

cd "$DATADIR"

for FILE in *; do
    gunzip "$FILE"
done
