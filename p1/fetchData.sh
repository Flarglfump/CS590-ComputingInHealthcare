#/usr/bin/bash

DATADIR="data" 

DATAFILE_URLS=(
    "https://www.encodeproject.org/files/ENCFF016INZ/@@download/ENCFF016INZ.bed.gz" # https://www.encodeproject.org/experiments/ENCSR975LGK/
    "https://www.encodeproject.org/files/ENCFF810SEM/@@download/ENCFF810SEM.bed.gz" # https://www.encodeproject.org/experiments/ENCSR437PXY/
    "https://www.encodeproject.org/files/ENCFF478ZBE/@@download/ENCFF478ZBE.bed.gz" # https://www.encodeproject.org/experiments/ENCSR534RXN/
    "https://www.encodeproject.org/files/ENCFF975INV/@@download/ENCFF975INV.bed.gz" # https://www.encodeproject.org/experiments/ENCSR208YDK/
    "https://www.encodeproject.org/files/ENCFF735ILY/@@download/ENCFF735ILY.bed.gz" # https://www.encodeproject.org/experiments/ENCSR875IVR/
    "https://www.encodeproject.org/files/ENCFF275TRN/@@download/ENCFF275TRN.bed.gz" # https://www.encodeproject.org/experiments/ENCSR242CLA/
    "https://www.encodeproject.org/files/ENCFF876SSA/@@download/ENCFF876SSA.bed.gz" # https://www.encodeproject.org/experiments/ENCSR892LQT/
    "https://www.encodeproject.org/files/ENCFF253LML/@@download/ENCFF253LML.bed.gz" # https://www.encodeproject.org/experiments/ENCSR636DIR/
    "https://www.encodeproject.org/files/ENCFF477UFH/@@download/ENCFF477UFH.bed.gz" # https://www.encodeproject.org/experiments/ENCSR154NYM/
    "https://www.encodeproject.org/files/ENCFF794YOT/@@download/ENCFF794YOT.bed.gz" # https://www.encodeproject.org/experiments/ENCSR582MYC/
)

if [ ! -d "$DATADIR" ]; then
    mkdir "$DATADIR"
fi

for i in "${!DATAFILE_URLS[@]}"; do
    wget "${DATAFILE_URLS[$i]}" "-O" "$DATADIR/data$i.bed.gz" 
done
