#/usr/bin/bash

SRCCEREFDIR="/proj/SIUE-CS590-490/reference"
REFDIR="/users/gwitske/CS590-ComputingInHealthcare/p1/reference"

if [ ! -d "$SRCCEREFDIR" ]; then
  echo "Source reference directory \"$SRCCEREFDIR\" does not exist!"
  exit
fi

if [ ! -d "$REFDIR" ]; then
  mkdir ${REFDIR}
fi

for FILE in $SRCCEREFDIR/*; do 
  cp $FILE $REFDIR
done