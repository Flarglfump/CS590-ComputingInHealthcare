#!/bin/bash

# Update environment, install htop and screen
sudo apt-get update
sudo apt-get install -y htop screen

# Setup miniconda
mkdir -p ~/miniconda3
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O ~/miniconda3/miniconda.sh
bash ~/miniconda3/miniconda.sh -b -u -p ~/miniconda3
rm -rf ~/miniconda3/miniconda.sh

if test ! -f ~/miniconda3/bin/conda; then
  echo "Could not find conda executable"
else
  echo "Initializing conda bash environment..."
  export PATH="~/miniconda3/bin:$PATH"
  conda init bash
fi

# Create, activate and export conda environment
conda create --name gwitske_env python=3.11 -y
source ~/.bashrc
conda activate gwitske_env