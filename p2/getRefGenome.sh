#/usr/bin/bash

SRCCEREFDIR="/proj/siue-cs590-490-PG0/reference_genome/"
REFDIR="reference"

if [ ! -d "$SRCCEREFDIR" ]; then
  echo "Source reference directory \"$SRCCEREFDIR\" does not exist!"
  exit
fi

if [ ! -d "$REFDIR" ]; then
  mkdir -p ${REFDIR}
fi

for FILE in $SRCCEREFDIR/*; do 
  cp $FILE $REFDIR
done