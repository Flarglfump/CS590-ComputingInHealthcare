#!/bin/bash

# Set up vars
MINICONDA_DIR="$HOME/miniconda3"
CONDA_EXE="$MINICONDA_DIR/bin/conda"

# Update environment, install htop and screen
sudo apt-get update
sudo apt-get install -y htop screen

# Setup miniconda
mkdir -p $MINICONDA_DIR
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O $MINICONDA_DIR/miniconda.sh
bash $MINICONDA_DIR/miniconda.sh -b -u -p $MINICONDA_DIR
rm -rf $MINICONDA_DIR/miniconda.sh

$CONDA_EXE init bash